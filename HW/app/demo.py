import serial
import time
from websocket import create_connection


turn_90=3
turn_180=6
one_step=5
ws = create_connection("ws://192.168.1.1:8887")

def turn_right(ser,times):
	ser.write('d'.encode())
	time.sleep(times)
	ser.write('s'.encode())
	time.sleep(0.1)


def turn_left(ser,times):
	ser.write('a'.encode())
	time.sleep(times)
	ser.write('s'.encode())
	time.sleep(0.1)

def forward(ser,times):
	ser.write('w'.encode())
	time.sleep(times)   #
	ser.write('s'.encode())
	time.sleep(0.1)

def demo():
	try:
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
	except:
		ser.close()
		time.sleep(2)
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
	#### 1-1	
	turn_left(ser,turn_90)
	forward(ser,10)
	time.sleep(1)
	turn_left(ser,turn_180)
	###
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()


	##### 1-2
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 1-3
	turn_right(ser,turn_180)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 1-4
	turn_right(ser,turn_180)
	forward(ser,one_step*2)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 2-1
	turn_right(ser,turn_180)
	forward(ser,10)
	turn_right(ser,turn_90)
	forward(ser,3)
	turn_left(ser,turn_90)
	forward(ser,3)
	time.sleep(1)
	turn_right(ser,turn_90/2)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 2-2
	turn_right(ser,turn_90/2)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_180)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/910"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 2-3
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_180)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/915"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 2-4
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_180)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/927"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 2-5
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/929"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 3-1
	forward(ser,10)
	turn_right(ser,turn_90)
	forward(ser,10)
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/919"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 3-2
	turn_right(ser,turn_180)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/916"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 3-3
	turn_right(ser,turn_180)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/918"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 3-4
	turn_right(ser,turn_180)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/908"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 3-5
	turn_right(ser,turn_180)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	time.sleep(1)
	turn_right(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/914"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 4-1
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_right(ser,turn_90)
	forward(ser,one_step)
	turn_left(ser,turn_90)
	forward(ser,one_step)
	time.sleep(1)
	turn_left(ser,turn_90)
	####
	ws.send('{"qrcode":"http://appls.ncut.edu.tw/KM/WebApi/Robot/GetPepperInfoV2/183"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()


