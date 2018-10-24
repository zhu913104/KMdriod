from websocket import create_connection
ws = create_connection("ws://192.168.141.116:8887")
print("Sending 'Hello, World'...")
ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/908"}'.encode())
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
