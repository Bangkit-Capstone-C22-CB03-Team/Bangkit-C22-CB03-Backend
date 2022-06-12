#! python
import os
import time
import re
from flask import Flask
from flask_restful import Resource, Api, reqparse
from predict_Func import predict_func

app = Flask(__name__)
api = Api(app)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def checkemail(email):
	if(re.fullmatch(regex, email)):
		return True
	return False

def getpartofday(hour):
    if (hour > 4) and (hour <= 12 ):
        return 'Pagi'
    elif (hour > 12) and (hour <= 16):
        return'Siang'
    elif (hour > 16) and (hour <= 20) :
        return 'Sore'
    elif (hour > 20) and (hour <= 24):
        return'Malam'
    elif (hour <= 4):
        return'Malam'

class TestPredict(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'msg', type=str, help='Cannot be empty', required=True, location='args')
        # location : body = "form"
        # location : querystring = "args"
        # location : headers = "headers"
        args = parser.parse_args()

        if("hai" in args['msg'].lower() or "hello" in args['msg'].lower() or "halo" in args['msg'].lower()):
            _, _, _, hour,_ = map(int, time.strftime("%Y %m %d %H %M").split())
            reply = "Hai, Selamat "+getpartofday(hour)+"! Perkenalkan nama saya SiLoka."
            return {'status': 'success', 'answer': reply}, 200

        else:
            answer, confidence = predict_func(args['msg'])
            if(confidence < 0.1):
                return {'status': 'failed', 'answer': answer, 'confidence': confidence}, 404
            
            if(checkemail(answer)):
                return {'status': 'success', 'answer': answer, 'confidence': confidence}, 200
            else:
                return {'status': 'success', 'answer': answer.capitalize(), 'confidence': confidence}, 200
    def get(self):
        return {'welcome': 'Selamat datang, apa yang bisa saya bantu?'}


api.add_resource(TestPredict, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
