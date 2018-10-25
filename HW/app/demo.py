import serial
import time
from websocket import create_connection


turn_90=4.5
turn_180=9.1
one_step=30
ws = create_connection("ws://192.168.1.1:8887")

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


def demo():
	try:
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
	except:
		ser.close()
		time.sleep(2)
		ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)


	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=1"}'.encode())
	result =  ws.recv()
	while result !='{"action": "next"}':
		print(result)
		result =  ws.recv()

	#### 1-1	
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

	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	###
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=1"}'.encode())
	result =  ws.recv()
	while result !='{"action": "next"}':
		print(result)
		result =  ws.recv()


	##### 1-2
	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=2"}'.encode())
	result =  ws.recv()
	while result!='{"action": "next"}':
		result =  ws.recv()

	##### 1-3
	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=3"}'.encode())
	result =  ws.recv()
	while result!='{"action": "next"}':
		result =  ws.recv()

	##### 1-4
	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=4"}'.encode())
	result =  ws.recv()
	while result!='{"action": "next"}':
		result =  ws.recv()


	##### 5
	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=5"}'.encode())
	result =  ws.recv()
	while result!='{"action": "next"}':
		result =  ws.recv()

	##### 6
	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	forward(ser)
	time.sleep(15)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	forward(ser)
	time.sleep(20)
	stopp(ser)
	
	
	right(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	time.sleep(2)
	
	right(ser)
	time.sleep(turn_90)
	stopp(ser)

	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=6"}'.encode())
	result =  ws.recv()
	while result!='{"action": "next"}':
		result =  ws.recv()

	##### 7
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
		
	time.sleep(2)

	right(ser)
	time.sleep(180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=7"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 8
	left(ser)
	time.sleep(turn_90)
	stopp(ser)	
		
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
		
	time.sleep(2)

	right(ser)
	time.sleep(180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=8"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()


	##### 9
	left(ser)
	time.sleep(turn_90)
	stopp(ser)	
		
	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)
		
	time.sleep(2)

	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=9"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 10
	left(ser)
	time.sleep(turn_90)
	stopp(ser)	
		
	forward(ser)
	time.sleep(17)
	stopp(ser)
	
	left(ser)
	time.sleep(3)
	stopp(ser)
		
	time.sleep(2)

	right(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=10"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()


	##### 11

	forward(ser)
	time.sleep(13)
	stopp(ser)
	
	left(ser)
	time.sleep(1.3)
	stopp(ser)

	forward(ser)
	time.sleep(23)
	stopp(ser)

	left(ser)
	time.sleep(turn_90)
	stopp(ser)
		
	time.sleep(2)

	left(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=11"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 12
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	forward(ser)
	time.sleep(58)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

		
	time.sleep(2)

	left(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=12"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 13
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

		
	time.sleep(2)

	left(ser)
	time.sleep(turn_180)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=13"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 14
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

	forward(ser)
	time.sleep(one_step)
	stopp(ser)
	
	left(ser)
	time.sleep(turn_90)
	stopp(ser)

		
	time.sleep(2)

	left(ser)
	time.sleep(turn_90)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=14"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()

	##### 15
	left(ser)
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
		
	left(ser)
	time.sleep(3.5)
	stopp(ser)

	forward(ser)
	time.sleep(10)
	stopp(ser)

	time.sleep(2)

	left(ser)
	time.sleep(6)
	stopp(ser)
	
	####
	ws.send('{"qrcode":"http://192.168.1.1:8080/qrcode.php?qrcode=14"}'.encode())
	result =  ws.recv()
	while result=='{"action": "next"}':
		result =  ws.recv()


