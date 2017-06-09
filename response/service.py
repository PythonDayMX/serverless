# -*- coding: utf-8 -*-
import uuid

from nodb import NoDB

def handler(event, context):
	
	code = event['params']['querystring'].get('code', None)

	if code:
		nodb = NoDB()
		nodb.serializer = "json"
		nodb.bucket = "pythondaymx"
		nodb.index = "code"
		obj = nodb.load(code)

		if obj:
			
			return {"statusCode": 200, "body": "ok", "response": obj}

		else:
			return {"statusCode": 404, "body": "Not found.", "obj":obj, "code":code}
	else:
		return {"statusCode": 400, "body": "Bad request."}