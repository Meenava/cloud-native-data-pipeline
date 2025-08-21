import unittest
from src.s3.s3_handler import S3Handler

class TestS3Handler(unittest.TestCase):

    def setUp(self):
        self.s3_handler = S3Handler()
        self.bucket_name = 'test-bucket'
        self.file_path = 'test_file.txt'
        self.file_key = 'test_file.txt'

    def test_upload_file(self):
        result = self.s3_handler.upload_file(self.bucket_name, self.file_path)
        self.assertTrue(result)

    def test_download_file(self):
        result = self.s3_handler.download_file(self.bucket_name, self.file_key)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()