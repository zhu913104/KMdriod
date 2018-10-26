from websocket import create_connection
ws = create_connection("ws://192.168.1.1:8887")
k=1
while True:
	result =  ws.recv()

	print('act' in result)
	if result =='{"act":"1"}':
		k=1
	elif result=='{"act":"0"}':
		k=0
	print("Received '%s'" % result)
