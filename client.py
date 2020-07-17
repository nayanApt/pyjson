#!/usr/bin/env python3

import socket
import json

HOST = '127.0.0.1'
PORT = 65432

class Laptop:
	pass

laptop = Laptop()
laptop.brand = 'MSI'
laptop.cpu = 'i7-7700HQ'

data = json.dumps(laptop.__dict__)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(bytes(data, encoding = "utf-8"))

	rcvd = s.recv(1024)
	rcvd = rcvd.decode("utf-8")

print('Sent :		{}'.format(data))
print('Received:	{}'.format(rcvd))