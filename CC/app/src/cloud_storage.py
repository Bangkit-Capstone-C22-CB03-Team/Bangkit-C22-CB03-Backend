import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

os.makedirs('./ml_model/', exist_ok=True)


def download_model():
    storage_client = storage.Client()

    bucket_name = 'latihan-cloud-bucket'

    bucket = storage_client.bucket(bucket_name)

    blobs = bucket.list_blobs(prefix='ml_model/')

    for blob in blobs:
        filename = blob.name.replace('ml_model/', '')
        if(len(filename) <= 0):
            continue
        if(os.path.isfile('ml_model/' + filename)):
            continue
        blob.download_to_filename("ml_model/" + filename)
