import serial
import time
from websocket import create_connection
import sys


step = sys.argv[1]
turn_90=4.5
turn_180=9.1
one_step=30

serverip = '192.168.141.16'
ws = create_connection("ws://"+serverip+":8887")




def forward(ser):
	ser.write("w".encode())
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'forward\r\n'.encode():
		ser.write("w".encode())
		ddd = ser.readline()
def right(ser):
	ser.write("a".encode())
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'right\r\n'.encode():
		ser.write("a".encode())
		ddd = ser.readline()


def left(ser):
	ser.write("d".encode())
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'left\r\n'.encode():
		ser.write("d".encode())
		ddd = ser.readline()


def back(ser):
	ser.write("s".encode())
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'back\r\n'.encode():
		ser.write("s".encode())
		ddd = ser.readline()

def stopp(ser):
	ser.write("q".encode())
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'stop\r\n'.encode():
		ser.write("q".encode())
		ddd = ser.readline()

def mstop(ws,tt):
	t = time.time()
	result =  ws.recv()
	k=1
	print("----5555-----")
	print(result)
	while ('act' in result)==False  :
		if result =='{"act":"1"}':
			k=1
			print("K=1")
		elif result=='{"act":"0"}':
			k=0
			print("K=0")
		result =  ws.recv()
		print("---------")
		print(result)

	print("warting....")
	while time.time()-t<tt :
		print(time.time()-t)
	while time.time()-t>tt :
		print(time.time()-t>tt)
		if k==1:
			print("PASS")
			pass
		elif k==0:
			print("break")
			sys.exit()
		else:
			print("warting....")
			
		


def demo(thing="gogo"):
	try:
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
	except:
		ser.close()
		time.sleep(2)
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)

	##### 15
	def ae():

		
		left(ser)
		time.sleep(turn_90)
		stopp(ser)


		time.sleep(2)

		right(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=15"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()


	##### 14
	def la():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		
		time.sleep(2)

		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=14"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		right(ser)
		time.sleep(turn_180)
		stopp(ser)

		forward(ser)
		time.sleep(17)
		stopp(ser)
	
		right(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(100)
		stopp(ser)


		ae()


	##### 13
	def cci():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		
		time.sleep(2)

		left(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=13"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()


		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		forward(ser)
		time.sleep(one_step)
		stopp(ser)


		la()


	##### 12
	def php():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		
		time.sleep(2)

		left(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=12"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()


		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		forward(ser)
		time.sleep(one_step)
		stopp(ser)

		cci()


	##### 11
	def cme():

		left(ser)
		time.sleep(turn_90)
		stopp(ser)
		
		time.sleep(2)

		left(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=11"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)

		forward(ser)
		time.sleep(58)
		stopp(ser)

		php()



	##### 10
	def me():

	
		left(ser)
		time.sleep(3)
		stopp(ser)
		
		time.sleep(2)

		right(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=10"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		forward(ser)
		time.sleep(13)
		stopp(ser)
	
		left(ser)
		time.sleep(1.3)
		stopp(ser)

		forward(ser)
		time.sleep(23)
		stopp(ser)


		cme()



	##### 9
	def air():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
		
		time.sleep(2)

		right(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=9"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)	
		
		forward(ser)
		time.sleep(17)
		stopp(ser)

		me()


	##### 8
	def dlim():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
		
		time.sleep(2)

		right(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=8"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)	
		
		forward(ser)
		time.sleep(one_step)
		stopp(ser)

		air()



	##### 7
	def ddm():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
		
		time.sleep(2)

		right(ser)
		time.sleep(turn_180)
		stopp(ser)
	
		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=7"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()
		
		left(ser)
		time.sleep(turn_90)
		stopp(ser)	
		
		forward(ser)
		time.sleep(one_step)
		stopp(ser)

		dlim()



	##### 6
	def ba():

	
	
		right(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		time.sleep(2)
	
		right(ser)
		time.sleep(turn_90)
		stopp(ser)

		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=6"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()
		forward(ser)
		time.sleep(one_step)
		stopp(ser)
		ddm()



	##### 5
	def mis():

	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		time.sleep(2)
	
		right(ser)
		time.sleep(turn_180)
		stopp(ser)

		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=5"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(15)
		stopp(ser)
	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(15)
		stopp(ser)

		ba()



	##### 1-4
	def iem():
	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		time.sleep(2)
	
		right(ser)
		time.sleep(turn_180)
		stopp(ser)

		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=4"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(one_step)
		stopp(ser)
		
		mis()


	##### 1-3
	def em():
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		time.sleep(2)
	
		right(ser)
		time.sleep(turn_180)
		stopp(ser)

		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=3"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(one_step)
		stopp(ser)
	
		iem()	

	##### 1-2
	def ee():
	
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		time.sleep(2)
	
		right(ser)
		time.sleep(turn_180)
		stopp(ser)

		####
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=2"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()

		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(one_step)
		stopp(ser)

		em()

		#### 1-1	
	def csie():
		print("left")
		left(ser)
		print("sleep")
		time.sleep(turn_90)
		print("stop")
		stopp(ser)
		print("sleep")
		time.sleep(2)
		print("right")
		right(ser)
		print("sleep")
		time.sleep(turn_180)
		stopp(ser)
	
		###
		ws.send(('{"qrcode":"http://'+serverip+'8080/qrcode.php?qrcode=1"}').encode())
		result = ' '
		result =  ws.recv()
		while result !='{"action": "next"}':
			print(result)
			result =  ws.recv()
		left(ser)
		time.sleep(turn_90)
		stopp(ser)
	
		forward(ser)
		time.sleep(one_step)
		stopp(ser)
		
		ee()
	def gogo():
		right(ser)
		time.sleep(turn_90)
		stopp(ser)

		forward(ser)
		time.sleep(one_step)
		stopp(ser)

		right(ser)
		time.sleep(turn_90)
		stopp(ser)

		forward(ser)
		time.sleep(one_step)
		stopp(ser)
		
		csie()
		
	
	if thing== "0":
		gogo()
	elif thing =='1':
		csie()
	elif thing =='2':
		ee()
	elif thing =='3':
		em()
	elif thing =='4':
		iem()
	elif thing =='5':
		mis()
	elif thing =='6':
		ba()
	elif thing =='7':
		ddm()
	elif thing =='8':
		dlim()
	elif thing =='9':
		air()
	elif thing =='10':
		me()
	elif thing =='11':
		cme()
	elif thing =='12':
		php()
	elif thing =='13':
		cci()
	elif thing =='14':
		la()
	elif thing =='15':
		ae()
	else :
		gogo()

if __name__ == "__main__":
	demo(step)
