from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
from cloud_storage import download_model

download_model('ml_model/', 'bert_model/')

# Load from our deployed model in Huggingface.co
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
