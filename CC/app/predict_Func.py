import sys
print(sys.version)

from transformers import pipeline
from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer

def predict_func(context):
  
  tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
  model = TFAutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad", return_dict = False)

  question = 'what country amazon forest is mostly in?'

  nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

  result = nlp(
      question = question,
      context = context
  )

  answer = result['answer']
  confidence = result['score']
  print(answer, '\n')
  print(confidence, '\n')

if __name__=="__main__":
  context = "The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain ""Amazonas"" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species."
  print(context, '\n')
  predict_func(context)