class S3Handler:
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def upload_file(self, bucket_name, file_path):
        try:
            file_name = file_path.split('/')[-1]
            self.s3_client.upload_file(file_path, bucket_name, file_name)
            print(f"File {file_name} uploaded to bucket {bucket_name}.")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, bucket_name, file_key):
        try:
            self.s3_client.download_file(bucket_name, file_key, file_key)
            print(f"File {file_key} downloaded from bucket {bucket_name}.")
        except Exception as e:
            print(f"Error downloading file: {e}")