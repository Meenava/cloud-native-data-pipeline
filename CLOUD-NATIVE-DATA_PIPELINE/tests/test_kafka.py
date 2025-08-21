import unittest
from src.kafka.producer import KafkaProducer
from src.kafka.consumer import KafkaConsumer

class TestKafka(unittest.TestCase):

    def setUp(self):
        self.producer = KafkaProducer()
        self.consumer = KafkaConsumer()

    def test_send_message(self):
        topic = 'test_topic'
        message = 'Hello, Kafka!'
        result = self.producer.send_message(topic, message)
        self.assertTrue(result)

    def test_consume_messages(self):
        topic = 'test_topic'
        self.producer.send_message(topic, 'Test message')
        messages = self.consumer.consume_messages(topic)
        self.assertIn('Test message', messages)

if __name__ == '__main__':
    unittest.main()