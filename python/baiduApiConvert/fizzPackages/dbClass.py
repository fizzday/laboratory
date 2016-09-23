#!/usr/bin/env python
#coding=utf8
from orator import DatabaseManager, Model

from fizzPackages.config import config

db = DatabaseManager(config.config())
Model.set_connection_resolver(db)

# print(config.test())
# exit()
class dbClass:

	def db():

		return db
