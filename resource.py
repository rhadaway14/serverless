import requests
import json
from flask import request, send_file
from flask_restful import Resource

# from http import HTTPStatus

class CL_Resource(Resource):
    """
    Confirm operation resource
    """
    def get(self):
        response = {"status": "totally connected bro"}
        return response, {'Access-Control-Allow-Origin': '*'} # something

class CL_DBBuild(Resource):
    """
    Populates DB on creation
    """
    def get(self):
        response = {"dbstatus": "populated"}
        return response, {'Access-Control-Allow-Origin': '*'}