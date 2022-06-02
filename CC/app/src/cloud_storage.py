import os
from google.cloud import storage

# service account key for read object in cloud storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


def download_model(bucket_folder, dest_folder):
    # make directory if not exist
    os.makedirs(dest_folder, exist_ok=True)

    storage_client = storage.Client()

    # bucket name from environment variable
    bucket_name = os.environ['BUCKET_NAME']

    bucket = storage_client.bucket(bucket_name)

    # list of blobs in the bucket folder
    blobs = bucket.list_blobs(prefix=bucket_folder)

    for blob in blobs:
        # every blob has <bucket_folder>/<blob_name>
        # we only want the blob name
        filename = blob.name.replace(bucket_folder, '')

        # this will skip if the blob only contain folder name
        if(len(filename) <= 0):
            continue

        # will skip if the file already exist
        if(os.path.isfile(dest_folder + filename)):
            continue

        # download the blob to the destination folder
        blob.download_to_filename(dest_folder + filename)
        print(f"Downloaded {filename}")
    print("Download complete")
