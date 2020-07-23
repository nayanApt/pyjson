#!/usr/bin/env python3

import server

if __name__ == '__main__':
	print('runserver module is being run directly')
	server.run()
else:
	print('runserver is being imported into another module')
