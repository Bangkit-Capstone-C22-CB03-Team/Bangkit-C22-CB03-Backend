import os
from google.cloud import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

db = firestore.Client()

def get_answer(categ_id,answer_id):
    docs = db.collection(u'answers').where(u'answerID', u'==', answer_id).where(u'categoryID', u'==', categ_id).stream()
    
    for doc in docs:
        answer = doc.to_dict()
        answer = answer['answer'].replace("\\n","\n")
        return answer

def get_context(categ_id):
    docs = db.collection(u'contexts').where(u'id', u'==', categ_id).stream()
    
    for doc in docs:
        context = doc.to_dict()
        return context['context']
