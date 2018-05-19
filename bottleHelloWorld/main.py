#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
bottle sample code.
Hello World !
main function
"""

import bottle



HOST = 'localhost'
PORT = 50000



# -----------------------------------------------------------------------------
@bottle.route('/hello')
def hello():
	"""
		hello
	"""
	return "Hello World!"



# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	bottle.run(host=HOST, port=PORT)
	return 0
