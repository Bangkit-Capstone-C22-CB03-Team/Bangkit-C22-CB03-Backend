from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# simple get rest api - test it by writing this on terminal with curl http://127.0.0.0:5000/
# or open this link http://127.0.0.0:5000/
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)