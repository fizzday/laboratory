#!/usr/bin/env python
#coding=utf8

class config:

	def config():
		
		config = {
		    'mysql': {
		        'driver': 'mysql',
		        'host': '127.0.0.1',
		        'database': 'test',
		        'user': 'fizz',
		        'password': 'Admin888,',
		        'prefix': ''
		    }
		}

		return config

	def test():
		return 333