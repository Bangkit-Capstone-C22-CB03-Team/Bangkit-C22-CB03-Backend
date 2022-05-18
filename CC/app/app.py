#! python
from flask import Flask
from flask_restful import Resource, Api, reqparse

from predict_Func import predict_func

app = Flask(__name__)
api = Api(app)

class TestPredict(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'chat', type=str, help='Cannot be empty', required=True)
        args = parser.parse_args()
        answer, confidence = predict_func(args['chat'])
        if(confidence< 0.5):
            return {'status': 'failed', 'answer': answer, 'confidence': confidence},404
        return {'status': 'success', 'answer': answer, 'confidence': confidence},200
    
    def get(self):
        return {'welcome': 'Welcome, what can I help you?'}


api.add_resource(TestPredict, '/')

if __name__ == '__main__':
    app.run()
