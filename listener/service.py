# -*- coding: utf-8 -*-
from nodb import NoDB

def handler(event, context):
	
	code = event['pathParameters'].get('proxy', None)

	if code:

		code = code.replace('/','')
		
		nodb = NoDB()
		nodb.serializer = "json"
		nodb.bucket = "pythondaymx"
		nodb.index = "code"

		obj = nodb.load(code)

		# Save object
		data = obj
		data['requests'].append(event)
		data['count'] = len(data['requests'])

		nodb.save(data)

		return {"statusCode": 200, "body": "created"}

	else:
		return {"statusCode": 200, "body": "Bad request."}