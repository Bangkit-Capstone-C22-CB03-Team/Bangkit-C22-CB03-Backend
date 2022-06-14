from google.cloud import firestore
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


db = firestore.Client()


def get_answers():
    docs = db.collection(u"answers")

    answers = []

    for doc in docs.stream():
        answers.append(doc.to_dict())
    return answers
