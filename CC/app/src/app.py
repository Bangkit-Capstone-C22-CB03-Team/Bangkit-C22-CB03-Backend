#! python
import os
import datetime
import pytz
import re
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from predict_Func import predict_func
from firestore import get_answers

app = Flask(__name__)
api = Api(app)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

answer_list = get_answers()


def checkemail(email):
    if(re.fullmatch(regex, email)):
        return True
    return False


def getpartofday(hour):
    if (hour > 4) and (hour <= 12):
        return 'Pagi'
    elif (hour > 12) and (hour <= 16):
        return'Siang'
    elif (hour > 16) and (hour <= 20):
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
        parser.add_argument(
            'categid', type=int, help='Cannot be empty', required=True, location='args')
        # location : body = "form"
        # location : querystring = "args"
        # location : headers = "headers"
        args = parser.parse_args()

        if(args['categid'] == 0):
<<<<<<< HEAD
            _, _, _, hour, _ = map(
                int, time.strftime("%Y %m %d %H %M").split())
            reply = "Hai, Selamat " + \
                getpartofday(hour)+"! Perkenalkan nama saya SiLoka."
=======
            hour =datetime.datetime.now(pytz.timezone('Asia/Jakarta')).hour
            reply = "Hai, Selamat "+getpartofday(hour)+"! Perkenalkan nama saya SiLoka."
>>>>>>> b5fc7cf78f420275066da69a6da22fe4bf98cee8
            return {'status': 'success', 'answer': reply}, 200

        else:
            answer, confidence = predict_func(args['msg'], args['categid'])
            res = [int(i) for i in answer.split() if i.isdigit()]
            if(res):
                # file = open(os.path.join('faq-ans/',"ans-categ"+str(args['categid'])+".json"),'r')
                # ans = json.loads(file.read())
                # for i in ans['answer_list']:
                #     if(i['id'] == res[0]):
                #         answer = i['answer']
                # file.close()
                for i in answer_list:
                    if(i["categoryID"] == args['categid'] and i["answerID"] == res[0]):
                        answer = i["answer"]
                return {'status': 'success', 'answer': answer, 'confidence': confidence}, 200
            else:
                return {'status': 'failed', 'answer': "Maaf saya tidak bisa mengerti pertanyaan anda atau informasi belum tersedia"}, 404

    def get(self):
        return {'welcome': 'Selamat datang, apa yang bisa saya bantu?'}


api.add_resource(TestPredict, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
