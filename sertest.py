import serial 
import time
import sys

side = sys.argv[1]
turn_time = float(sys.argv[2])

ser = serial.Serial("/dev/ttyACM0",9600,timeout=1)


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



if ser.isOpen():
	if side == 'w':
		forward(ser)
	elif side =='d':
		left(ser)
	elif side =='a':
		right(ser)
	elif side =='s':
		back(ser)
	else:
		stopp(ser)
	t= time.time()
	time.sleep(turn_time)
	"""ser.write(side.encode())
	ddd = ser.readline()
	while ddd != 'right'.encode():
		ser.write(side.encode())
		ddd = ser.readline()
	print(ddd)
	print("OK")	
	time.sleep(turn_time)
	ser.flushInput()
	ddd = ser.readline()
	while ddd != 'stop'.encode():
		ser.write("q".encode())
		ddd = ser.readline()
		print(ddd.decode()+"   NOTOK")"""
	stopp(ser)
	print(time.time()-t)

