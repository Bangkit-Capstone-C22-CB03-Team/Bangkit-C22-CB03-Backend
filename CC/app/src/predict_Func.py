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


def predict_func(question):

    context = "Makanan kesukaan saya adalah rendang."

    result = nlp(
        question=question,
        context=context
    )

    answer = result['answer']
    confidence = result['score']
    return answer, confidence
