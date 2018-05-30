import  cv2
import numpy as np
from PIL import Image
import zbarlight
from bs4 import BeautifulSoup
import requests
import datetime
import time

cap = cv2.VideoCapture(1)

code=""
def qrcode():
	while(cap.read()):
	    # 讀進來之做高斯模糊  然後Canny再抓輪廓
	    _,frame = cap.read()
	    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    img_gray = cv2.equalizeHist(img_gray)

	    th, bi_img = cv2.threshold(img_gray, 125, 255, cv2.THRESH_BINARY)

	    img_gb = cv2.GaussianBlur(img_gray, (3, 3), 0)

	    edges = cv2.Canny(img_gb, 100 , 200)

	    img_fc, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	    # 遞迴每個特徵  把鑲嵌層數大於五的取出來
	    try:
                hierarchy = hierarchy[0]
		found = []
		for i in range(len(contours)):
		    k = i
		    c = 0
		    while hierarchy[k][2] != -1:
		        k = hierarchy[k][2]
		        c = c + 1
		    if c >= 5:
		        found.append(i)
		draw_img = frame.copy()

		# 把把鑲嵌層數大於五的取出來  minAreaRect取平行四邊形包起來
		boxes = []
		# 把把鑲嵌層數大於五的取出來  minAreaRect取平行四邊形包起來
		# 得到四個邊點後畫圖
		for i in found:
		    rect = cv2.minAreaRect(contours[i])
		    box = cv2.boxPoints(rect)
		    box.tolist()
		    for i in range(len(box)):
		        xx = []
		        for x in box:
		            for y in x:
		                xx.append(y)
		    box = np.int0(box)
		    cv2.drawContours(draw_img, [box], 0, (0, 255, 0), 2)


		    boxes.append(box)


		def Vector2angle(v1, v2=(1, 0),degrees360 = False):
		    '''輸入兩個向量回傳夾角
		    degree360可以讓夾角超過180
		    也可以單純只輸入一個向量來求與X軸的夾角'''
		    try:
		        v2 = np.array(v2)
		        cos_angle = v1.dot(v2) / (np.sqrt(v1.dot(v1)) * np.sqrt(v2.dot(v2)))
		        Diametermetric = np.arccos(cos_angle)
		        angle = Diametermetric * 360 / 2 / np.pi
		        if degrees360:
		            if v1[1]>0:
		                angle = 360-angle
		        return angle
		    except:
		        return None

		def outerrectangle(pointlist):
		    # 輸入三個中心點  回傳一個矩形放大後的的四個點
		    pointlist = np.array(pointlist)
		    for i in range(len(pointlist)):
		        l1 = pointlist[i - 1] - pointlist[i]
		        l2 = pointlist[i - 2] - pointlist[i]
		        angle = Vector2angle(l1, l2)
		        if angle > 80 and angle < 100:
		            p4 = pointlist[i] + l1 + l2
		            cv2.circle(draw_img, (p4[0], p4[1]), 5, (0, 255, 255), -1)
		            fourpoint = np.array([pointlist[i - 1], pointlist[i], pointlist[i - 2], p4])
		            centerpoint = np.mean(fourpoint, axis=0)
		            o1 = (pointlist[i - 1] - centerpoint) * .5 + pointlist[i - 1]
		            o2 = (pointlist[i] - centerpoint) * .5 + pointlist[i]
		            o3 = (pointlist[i - 2] - centerpoint) * .5 + pointlist[i - 2]
		            o4 = (p4 - centerpoint) * .5 + p4
		            outerpoint = [o1, o2, o3, o4]
		            degree = Vector2angle(p4 - centerpoint, degrees360=True)
		            if degree>90 and  degree<135:
		                outerpoint = [o3, o2, o1, o4]
		            elif degree>225 and  degree<270:
		                outerpoint = [o3, o2, o1, o4]
		            elif degree>0 and  degree<45:
		                outerpoint = [o3, o2, o1, o4]
		            elif degree>315 and  degree<360:
		                outerpoint = [o3, o2, o1, o4]
		            else:
		                pass
		            outerpoint = np.int0(outerpoint)
		            cv2.drawContours(draw_img, [outerpoint], 0, (0, 0, 255), 2)
		            return outerpoint
		# 兩點距離
		def cv_distance(P, Q):
		    return int(np.sqrt(pow((P[0] - Q[0]), 2) + pow((P[1] - Q[1]), 2)))
		def createLineIterator(P1, P2, img):
		    """
		       Produces and array that consists of the coordinates and intensities of each pixel in a line between two points

		       Parameters:
		           -P1: a numpy array that consists of the coordinate of the first point (x,y)
		           -P2: a numpy array that consists of the coordinate of the second point (x,y)
		           -img: the image being processed

		       Returns:
		           -it: a numpy array that consists of the coordinates and intensities of each pixel in the radii (shape: [numPixels, 3], row = [x,y,intensity])     
		       """
		    # define local variables for readability
		    imageH = img.shape[0]
		    imageW = img.shape[1]
		    P1X = P1[0]
		    P1Y = P1[1]
		    P2X = P2[0]
		    P2Y = P2[1]

		    # difference and absolute difference between points
		    # used to calculate slope and relative location between points
		    dX = P2X - P1X
		    dY = P2Y - P1Y
		    dXa = np.abs(dX)
		    dYa = np.abs(dY)

		    # predefine numpy array for output based on distance between points
		    itbuffer = np.empty(shape=(np.maximum(dYa, dXa), 3), dtype=np.float32)
		    itbuffer.fill(np.nan)

		    # Obtain coordinates along the line using a form of Bresenham's algorithm
		    negY = P1Y > P2Y
		    negX = P1X > P2X
		    if P1X == P2X:  # vertical line segment
		        itbuffer[:, 0] = P1X
		        if negY:
		            itbuffer[:, 1] = np.arange(P1Y - 1, P1Y - dYa - 1, -1)
		        else:
		            itbuffer[:, 1] = np.arange(P1Y + 1, P1Y + dYa + 1)
		    elif P1Y == P2Y:  # horizontal line segment
		        itbuffer[:, 1] = P1Y
		        if negX:
		            itbuffer[:, 0] = np.arange(P1X - 1, P1X - dXa - 1, -1)
		        else:
		            itbuffer[:, 0] = np.arange(P1X + 1, P1X + dXa + 1)
		    else:  # diagonal line segment
		        steepSlope = dYa > dXa
		        if steepSlope:
		            slope = dX.astype(np.float32) / dY.astype(np.float32)
		            if negY:
		                itbuffer[:, 1] = np.arange(P1Y - 1, P1Y - dYa - 1, -1)
		            else:
		                itbuffer[:, 1] = np.arange(P1Y + 1, P1Y + dYa + 1)
		            itbuffer[:, 0] = (slope * (itbuffer[:, 1] - P1Y)).astype(np.int) + P1X
		        else:
		            slope = dY.astype(np.float32) / dX.astype(np.float32)
		            if negX:
		                itbuffer[:, 0] = np.arange(P1X - 1, P1X - dXa - 1, -1)
		            else:
		                itbuffer[:, 0] = np.arange(P1X + 1, P1X + dXa + 1)
		            itbuffer[:, 1] = (slope * (itbuffer[:, 0] - P1X)).astype(np.int) + P1Y

		    # Remove points outside of image
		    colX = itbuffer[:, 0]
		    colY = itbuffer[:, 1]
		    itbuffer = itbuffer[(colX >= 0) & (colY >= 0) & (colX < imageW) & (colY < imageH)]

		    # Get intensities from img ndarray
		    itbuffer = img[itbuffer[:, 1].astype(np.uint), itbuffer[:, 0].astype(np.uint)]

		    return itbuffer
		def isTimingPattern(line):
		    # 去除開頭的白色
		    while line[0] != 0:
		        line = line[1:]
		    while line[-1] != 0:
		        line = line[:-1]
		    # 計算連續的黑白像素點
		    c = []
		    count = 1
		    l = line[0]
		    for p in line[1:]:
		        if p == l:
		            count = count + 1
		        else:
		            c.append(count)
		            count = 1
		        l = p
		    c.append(count)
		    # 如果黑白間隔太少，直接排除
		    if len(c) < 5:
		        return False
		    # 計算方差，根据離散程度判断是否是 Timing Pattern
		    threshold = 5
		    return np.var(c) < threshold
		def check(a, b,img):
		    # 存 a b 之間最短距離座標
		    s1_ab = ()
		    s2_ab = ()
		    # 存 a b 之間最短距離座標距离，np.iinfo('i').max取的 INT最大值
		    s1 = np.iinfo('i').max
		    s2 = s1
		    for ai in a:
		        for bi in b:
		            d = cv_distance(ai, bi)
		            if d < s2:
		                if d < s1:
		                    s1_ab, s2_ab = (ai, bi), s1_ab
		                    s1, s2 = d, s1
		                else:
		                    s2_ab = (ai, bi)
		                    s2 = d

		    try:
		        #把線往下沿一點
		        a1, a2 = s1_ab[0], s2_ab[0]
		        b1, b2 = s1_ab[1], s2_ab[1]
		        a1 = (a1[0] + (a2[0] - a1[0]) // 14, a1[1] + (a2[1] - a1[1]) // 14)
		        b1 = (b1[0] + (b2[0] - b1[0]) // 14, b1[1] + (b2[1] - b1[1]) // 14)
		        a2 = (a2[0] + (a1[0] - a2[0])  // 14, a2[1] + (a1[1] - a2[1]) // 14)
		        b2 = (b2[0] + (b1[0] - b2[0])  // 14, b2[1] + (b1[1] - b2[1]) // 14)

		        # 把最短的两个線畫出来
		        line1 = createLineIterator(a1, b1, img)
		        line2 = createLineIterator(a2, b2, img)
		        if isTimingPattern(line1):
		            cv2.line(draw_img, a1, b1, (0, 0, 255), 3)
		            return True
		        if isTimingPattern(line2):
		            cv2.line(draw_img, a2, b2, (0, 0, 255), 3)
		            return True
		    except:
		        pass
		# 取得i 跟 他的下一個的四個點一起比較
		valid = set()
		for i in range(len(boxes)):
		    for j in range(i+1, len(boxes)):
		        if check(boxes[i], boxes[j],bi_img):
		            valid.add(i)
		            valid.add(j)

		point_all = []
		center_all = []
	       #求3個QRCODE編框的中心點
		while len(valid)==3:
		    for i in range(len(valid)):
		        rect = cv2.minAreaRect(contours[found[valid.pop()]])
		        box = cv2.boxPoints(rect)
		        box.tolist()
		        for i in range(len(box)):
		            xx = []
		            for x in box:
		                for y in x:
		                    xx.append(y)
		        box = np.int0(box)
		        cv2.drawContours(draw_img, [box], 0, (0, 255, 0), 2)
		        center = [int((xx[0] + xx[2] + xx[4] + xx[6]) // 4), int((xx[1] + xx[3] + xx[5] + xx[7]) // 4)]
		        center_all.append(center)
		        center = tuple(center)
		        cv2.circle(draw_img, center, 5, (0, 255, 255), -1)

		    break

		while outerrectangle(center_all) is not None:
		    pts1 = outerrectangle(center_all)
		    pts1 = np.float32(pts1)
		    pts2 = np.float32([[300,0],[0,0],[0,300],[300,300]])
		    M = cv2.getPerspectiveTransform(pts1, pts2)
		    dst = cv2.warpPerspective(bi_img, M, (300, 300))
		    cv2.imshow("xxxxx", dst)
		    cv2.imwrite("QR000.jpg",dst)
		    file_path = "QR000.jpg"
		    with open (file_path, 'rb')as image_file:
		        image = Image.open(image_file)
		        image.load()
		    codes = zbarlight.scan_codes("qrcode",image)
		    print("CODES: ",codes)
		    for i in codes:
		        print("decode: ",i.decode("utf-8"))
		    break
		cv2.imshow("xx",draw_img)
		cv2.imshow("edges",)

		if cv2.waitKey(1) & 0xFF == 27:
		    break
	    except:
		pass
	cap.release()
	cv2.destroyAllWindows()
while __init__="__main"__:
      qrcode()
