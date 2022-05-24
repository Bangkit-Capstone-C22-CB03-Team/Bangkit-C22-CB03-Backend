import json
import os

def get_titles(jsons):
    """Append titles value from json file into a list"""
    with open(jsons, encoding="utf-8") as json_file:
        titles = []
        file = json.load(json_file)
        translated = file
        data = translated['data']
        for key in data:
            titles.append(key['title'])
        return titles

def split_list(lst, length):
    """Yield successive length-sized chunks from list"""
    for i in range(0, len(lst), length):
        yield lst[i:i + length]

def create_batch_dict(lst, length):
    """Convert list of list into dictionary and creates new keys called batch1 to batch split-length"""
    split=list(split_list(lst, length))
    dict_batch = {}
    x = 1
    for batches in split:
        dict_batch[f"batch{x}"] = batches
        x += 1
    return dict_batch

dirname = os.path.dirname(os.path.abspath(__file__))
json_source = os.path.join(dirname, 'SourceFile', 'dev-v2.0.json')

# Get titles, create batch dict from the titles, then generate batches vars with the appropriate values(titles)
lst = get_titles(json_source)
d = create_batch_dict(lst, 7)
count = 1
for key,val in d.items():
    exec(key + '=val')
    count += 1

# Print out the batches vars with its values
batchs = []
for z in range(1, count):
    batchs.append(f'batch{z}')
for batch in batchs:
    print(batch)
    print(vars()[batch])
    print ('')