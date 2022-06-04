import os
from google.cloud import storage

# service account key for read object in cloud storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service-acc/qwiklabs-gcp-01-fd99dfad1c8a-770e3fc2ef69.json'

storage_client = storage.Client()

def download_file_from_bucket(bucketname,bucket_folder, save_path):
    os.makedirs(save_path, exist_ok=True)
    
    try:
        bucket = storage_client.get_bucket(bucketname)
        blobs = bucket.list_blobs(prefix=bucket_folder)

        for blob in blobs:
            filename = blob.name.split("/")
            blob.download_to_filename(os.path.join(save_path,filename[1]))

        return True
    except Exception as e:
        print(e)
        return False
