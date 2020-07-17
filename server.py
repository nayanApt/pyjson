#!/usr/bin/env python3

import socket
import json

HOST = '127.0.01'
PORT = 65432

class Laptop:
	pass

laptop = Laptop()
laptop.model = 'GV62-7RE'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by: ',addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			data = json.loads(data)
			if data["brand"] == 'MSI' and data["cpu"] == 'i7-7700HQ':
				conn.sendall(bytes(laptop.model, encoding = "utf-8"))
			else:
				conn.sendall(bytes('Not found', encoding = "utf-8"))
