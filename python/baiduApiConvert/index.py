#!/usr/bin/env python
#coding=utf8
import sys, os
sysDir =  os.path.dirname(os.getcwd())
sys.path.append(sysDir)

from fizzPackages.dbClass import dbClass
db = dbClass.db()

from fizzPackages.Model.User import User

# user = User.find(1)

# # print(users.to_dict())
# print(user.name)
# exit()


users = db.table('users').where({'id':1, 'name':'lily'}).first()
# users = User.where([['id', '>', '1']]).get()
print(users)
# for user in users:
#     print(user[0])