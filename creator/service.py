# -*- coding: utf-8 -*-
import uuid

from nodb import NoDB

def createCode():
	code = str(uuid.uuid4().get_hex()[0:8])

	# check if code exists
	nodb = NoDB()
	nodb.serializer = "json"
	nodb.bucket = "pythondaymx"
	nodb.index = "code"

	obj = nodb.load(code)
	
	if obj:
		code = createCode()
	else:
		data = {
			"code": code,
			"requests": [],
			"count":0
		}
		nodb.save(data)
	return code

def handler(event, context):

	code = createCode()

	return {"statusCode": 200, "body": "ok", "code":code}