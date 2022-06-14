import os
import json
import datetime
from datetime import timezone
import requests
import uuid
from chalice import Blueprint
from chalice import Response
from chalicelib.dbConnections import getDbConnection
from chalicelib.miscFunctions import processError

mainService = Blueprint(__name__)

DEBUG_LOG_ENABLE = False

UNKNOWN_MSG_TYPE = 'unknown message type'
UNKNOWN_MSG_VER = 'unknown message version'
PARAMETER_MISSING = 'parameter missing'
DATABASE_ERROR = 'database error'
API_ERROR = 'api error'
UNKNOWN_ERROR = 'unknown error'

@mainService.route('/mainService/v1/example', methods=['POST'], cors=True)
def examplePostProcessing():
    responseMessage = {}
    responseSubMessage = {}
    try:
        payload = mainService.current_request.json_body
        id = payload['id']
        key = payload['key']

        responseSubMessage['data'] = 'kfjflkjlksfjlfjl'
        responseMessage['type'] = 'success'
        responseMessage['message'] = responseSubMessage
        return Response(body=responseMessage, status_code=200, headers={'Content-Type': 'application/json'})

    except Exception as e:
        responseSubMessage['errorCode'] = 1
        responseSubMessage['errorMessage'] = '%s parameter missing' % e
        responseMessage['type'] = 'error'
        responseMessage['message'] = responseSubMessage
        return Response(body=responseMessage, status_code=400, headers={'Content-Type': 'application/json'})