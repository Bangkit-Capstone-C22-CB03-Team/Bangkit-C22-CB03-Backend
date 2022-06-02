import os
from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service-acc/qwiklabs-gcp-02-96ccf592dc5f-c92d453542da.json'
storage_client = storage.Client()

os.makedirs('./bert_model/', exist_ok=True)


def donwload_model_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False


donwload_model_from_bucket('bert_model/config.json', os.path.join(
    'bert_model/', 'config.json'), 'qwiklabs-gcp-02-96ccf592dc5f-test-bucket')
donwload_model_from_bucket('bert_model/tf_model.h5', os.path.join(
    'bert_model/', 'tf_model.h5'), 'qwiklabs-gcp-02-96ccf592dc5f-test-bucket')

# Load from our deployed model in Huggingface.co
tokenizer = AutoTokenizer.from_pretrained(
    "Andaf/bert-uncased-finetuned-squad-indonesian")

model = TFAutoModelForQuestionAnswering.from_pretrained(
    './bert_model/', return_dict=False)

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
