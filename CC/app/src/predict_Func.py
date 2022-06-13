import json
from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline

from config import BUCKET_NAME, BUCKET_FOLDER
from cloud_storage import download_file_from_bucket

download_file_from_bucket(BUCKET_NAME, BUCKET_FOLDER, 'bert_model/')

# Load from our deployed model in from Google Cloud Storage
tokenizer = AutoTokenizer.from_pretrained(
    "./bert_model/")
model = TFAutoModelForQuestionAnswering.from_pretrained(
    "./bert_model/", return_dict=False)

nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)


def predict_func(question,categid):

    f = open('context.json','r')
    data = json.loads(f.read())

    for i in data['context_list']:
        if(i['id'] == categid):
            context = i['context']
            break
    
    f.close()

    result = nlp(
        question=question,
        context=context
    )

    answer = result['answer']
    confidence = result['score']
    return answer, confidence

# print(predict_func("Apa itu biaya layanan?",1))