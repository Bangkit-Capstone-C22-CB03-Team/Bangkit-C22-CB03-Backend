from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline

# Load from our deployed model in Huggingface.co
tokenizer = AutoTokenizer.from_pretrained(
    "Andaf/bert-uncased-finetuned-squad-indonesian")
model = TFAutoModelForQuestionAnswering.from_pretrained(
    "Andaf/bert-uncased-finetuned-squad-indonesian", return_dict=False)

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
