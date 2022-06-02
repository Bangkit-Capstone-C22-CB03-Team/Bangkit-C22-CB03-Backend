import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'SERVICEKEYJSON '

storage_client = storage.Client()

# Create New bucket

bucket_name = 'qwiklabs-gcp-02-112c2c205567_data_bucket'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)

# Accessing a Specific bucket

my_bucket = storage_client.get_bucket('qwiklabs-gcp-02-112c2c205567_data_bucket')

# upload Files

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket('qwiklabs-gcp-02-112c2c205567_data_bucket')
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r'C:\Users\user\OneDrive\Documents\Project Capstone\Bangkit-C22CB-Company-Based-Capstone\CC\app\src\bert_model'
upload_to_bucket('bert_model/config', os.path.join(file_path,'config.json'), 'qwiklabs-gcp-02-112c2c205567_data_bucket')
upload_to_bucket('bert_model/tf_model', os.path.join(file_path,'tf_model.h5'), 'qwiklabs-gcp-02-112c2c205567_data_bucket')


# Download files

def donwload_file_from_bucket(blob_name,file_path,bucket_name):
    try:
        bucket = storage_client.get_bucket('qwiklabs-gcp-02-112c2c205567_data_bucket')
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False

donwload_file_from_bucket('config', os.path.join(os.getcwd(),'file1.json'),'qwiklabs-gcp-02-112c2c205567_data_bucket')