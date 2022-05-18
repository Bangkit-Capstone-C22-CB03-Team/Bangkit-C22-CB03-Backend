import json
import os
from deep_translator import GoogleTranslator
from SQuAD_trans_utils import get_titles, create_batch_dict


# Hyperparameter
dirname = os.path.dirname(os.path.abspath(__file__))
json_source = os.path.join(dirname, 'SourceFile', 'dev-v2.0.json')
json_dest = os.path.join(dirname, 'Translated', 'dev-v2.0_indo.json')
lang_source = 'en'
lang_dest = 'id'

# Get titles, create batch dict from the titles, then generate batches vars with the appropriate values(titles)
lst = get_titles(json_source)
d = create_batch_dict(lst, 7)
for key,val in d.items():
    exec(key + '=val')

# Batch Selector
chosen_batch = batch1 #ignore the warning because the variable is generated not created manually

# When the first batch is done, the source JSON file will be changed to the dest JSON file to continue the progress
if chosen_batch is not batch1:
    json_source = json_dest

# Instantiate the google translator
my_translator = GoogleTranslator(source=lang_source, target=lang_dest)

# Indicator
console_count = 0


""" Loads the JSON file that needs to be dict_file after that it converts the JSON file 
into python dictionary and lastly it starts crawling into the keys as well as translating 
the values into the  """ 

with open(json_source, encoding="utf-8") as json_file:
    file = json.load(json_file)
    dict_file = file
    data = dict_file['data']

    for key in data:
        if key['title'] in chosen_batch:
            title = key['title']
            translations = my_translator.translate(text=title)
            key['title'] = translations
            paragraphs = key['paragraphs']

            for key in paragraphs:
                qas = key['qas']
                context = key['context']
                translations = my_translator.translate(text=context)
                key['context'] = translations

                for key in qas:
                    question = key['question']
                    translations = my_translator.translate(text=question)
                    key['question'] = translations
                    answers = key['answers']

                    for keys in answers:
                        text = keys['text']
                        print(text)
                        translations = my_translator.translate(text=text)
                        keys['text'] = translations
                        print(console_count)
                        console_count += 1

                    if 'plausible_answers' in key:
                        plausible_answers = key['plausible_answers']
                        for keys in plausible_answers:
                            text = keys['text']
                            translations = my_translator.translate(text=text)
                            keys['text'] = translations

# Save the translated dict_file into translated variable
translated = dict_file


""" Creates new JSON file and dumps the dict_file JSON source into the new JSON file """

with open(json_dest, 'w', encoding="utf-8") as fout:
    json_dumps_str = json.dumps(translated, indent=4, ensure_ascii=False)
    fout.write(json_dumps_str)
    print ("DONE")
