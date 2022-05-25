import pandas as pd

def json_to_df(data):
    '''Convert dataset json file to pandas dataframe

    Args:
        data (json): json file of the dataset

    Returns:
        df (pandas dataframe): dataframe of the dataset
    '''
    # create empty dataframe
    dataset_df = pd.DataFrame()

    # iterate through data
    for key in data:
        title = key['title']
        paragraphs = key['paragraphs']
        for key in paragraphs:
            qas = key['qas']
            context = key['context']
            for key in qas:
                input_id = key['id']
                question = key['question']
                answers = key['answers']
                dataset_df = dataset_df.append({
                    'input_id': input_id,
                    'title': title,
                    'context': context,
                    'question': question,
                    'answers': answers
                    }, ignore_index=True)
    return dataset_df