# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client['admin']

db.authenticate('root', '123456')

print db.collection_names()