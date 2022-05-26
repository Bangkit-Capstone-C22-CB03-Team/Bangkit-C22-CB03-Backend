#! python
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse

from predict_Func import predict_func

app = Flask(__name__)
api = Api(app)

class TestPredict(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'msg', type=str, help='Cannot be empty', required=True,location='args')
            # location : body = "form"
            # location : querystring = "args"
            # location : headers = "headers"
        args = parser.parse_args()
        answer, confidence = predict_func(args['msg'])
        if(confidence< 0.1):
            return {'status': 'failed', 'answer': answer, 'confidence': confidence},404
        return {'status': 'success', 'answer': answer, 'confidence': confidence},200
    
    def get(self):
        return {'welcome': 'Welcome, what can I help you?'}


api.add_resource(TestPredict, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
