#! python

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
# lib ini buat akses .env file
from decouple import config

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config("DB_USER")}:{config("DB_PASS")}@{config("DB_HOST")}/{config("DB_DATABASE")}'
# config sqlalchemy_track_modifications agar notif deprecation warning tidak tampil
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Schema
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)

    # return agar menjadi json bukan jadi object class
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone
        }


db.create_all()

# API
class ShowData(Resource):
    def get(self):
        users = User.query.all()
        return {
            'status': 'success',
            'data': [
                # map agar data ditampilkan berupa json
                user.to_json() for user in users
            ]
        }, 200

    def post(self):
        name = request.json['name']
        phone = request.json['phone']
        # buat data untuk disimpan ke databse
        add_data = User(name=name, phone=phone)
        # simpan ke session (supaya sekali query jika menyimpan banyak data)
        db.session.add(add_data)
        # simpan ke database
        db.session.commit()
        return {
            'status': 'success',
            'message': 'Data berhasil ditambahkan'
        }, 201
    

api.add_resource(ShowData, '/')

if __name__ == '__main__':
    app.run()