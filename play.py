from websocket import create_connection
import sys


step = sys.argv[1]
ws = create_connection("ws://172.16.1.3:8887")



def play(step):
	url = '{"qrcode":"http://172.16.1.3:8080/qrcode.php?qrcode='+step+'"}'
	ws.send(url.encode())


if __name__ == "__main__":
	play(step)
