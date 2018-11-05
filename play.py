from websocket import create_connection
import sys


step = sys.argv[1]
serverip = '192.168.141.16'
ws = create_connection("ws://"+serverip+":8887")



def play(step):
	url = '{"qrcode":"http://'+serverip+':8080/qrcode.php?qrcode='+step+'"}'
	ws.send(url.encode())


if __name__ == "__main__":
	play(step)
