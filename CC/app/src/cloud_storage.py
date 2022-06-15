import os
from google.cloud import storage

# service account key for read object in cloud storage
# set this if you want to try in local, comment if deploy to cloud run
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

storage_client = storage.Client()

def download_file_from_bucket(bucket_name, bucket_folder, save_path):
    os.makedirs(save_path, exist_ok=True)

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=bucket_folder)
        for blob in blobs:
            # print(f"{blob.name},{blob.generation}")
            filename = blob.name.split("/")
            if filename[1] == "":
                continue
            if os.path.isfile(os.path.join(save_path, filename[1])):
                continue
            blob.download_to_filename(os.path.join(save_path, filename[1]))

        return True
    except Exception as e:
        print(e)
        return False
