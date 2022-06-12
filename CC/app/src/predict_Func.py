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

    context = "Sisa kamar hotel: 12. Kondisi hotel bersih, ruang resepsionis tidak ramai. Pembayaran dapat dilakukan melalui transfer bank atau membayar melalui minimarket. Penjadwalan ulang flight booking dapat dilakukan dengan mengirim email. Kirim email ke customer-service@traveloka.com"

    result = nlp(
        question=question,
        context=context
    )

    answer = result['answer']
    confidence = result['score']
    return answer, confidence
