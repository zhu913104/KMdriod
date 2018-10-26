from websocket import create_connection
ws = create_connection("ws://172.16.1.3:8887")
ws.send('{"qrcode":"http://172.16.1.3:8080/qrcode.php?qrcode=1"}'.encode())
