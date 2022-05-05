import os
from google.cloud import storage


def get_storage_client():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'My_ServiceKey_GoogleCloud.json'
    s_client = storage.Client()
    return s_client


def set_bucket(s_client, bucket_name):
    bucket = s_client.bucket(bucket_name)
    bucket.location = 'UZB'
    bucket = s_client.create_bucket(bucket)
    return bucket


def upload_file(s_client, blob_name, file_path, bucket_name):
    try:
        bucket = s_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False


def download_file_from_bucket(s_client, blob_name, file_path, bucket_name):
    try:
        bucket = s_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            s_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    storage_client = get_storage_client()

    # my_bucket = storage_client.get_bucket('lexx-quotes-test')
    # print(vars(my_bucket))

    download_file_from_bucket(storage_client, 'top200quotes.csv',
                              os.path.join(os.getcwd(), 'result.csv'), 'lexx-quotes-test')
