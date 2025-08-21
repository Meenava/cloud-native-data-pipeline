import unittest
from src.database.nosql_connector import NoSQLConnector

class TestNoSQLConnector(unittest.TestCase):

    def setUp(self):
        self.connector = NoSQLConnector()
        self.collection_name = "test_collection"
        self.test_document = {"name": "test", "value": 123}

    def test_insert_document(self):
        result = self.connector.insert_document(self.collection_name, self.test_document)
        self.assertTrue(result)

    def test_fetch_documents(self):
        self.connector.insert_document(self.collection_name, self.test_document)
        query = {"name": "test"}
        documents = self.connector.fetch_documents(self.collection_name, query)
        self.assertGreater(len(documents), 0)
        self.assertEqual(documents[0]["name"], "test")

    def tearDown(self):
        # Clean up the test collection after each test
        self.connector.delete_collection(self.collection_name)

if __name__ == '__main__':
    unittest.main()