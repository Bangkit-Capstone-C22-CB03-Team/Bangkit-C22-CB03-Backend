from google.cloud import firestore
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


db = firestore.Client()

docs = db.collection(u"answers")

answers = []
for doc in docs.stream():
    answers.append(doc.to_dict())

answers.sort(key=lambda x: x["answerID"])

for i in answers:
    print(i["answerID"])
