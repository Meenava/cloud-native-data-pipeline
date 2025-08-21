class KafkaProducer:
    def __init__(self, bootstrap_servers, topic):
        from kafka import KafkaProducer
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.topic = topic

    def send_message(self, message):
        self.producer.send(self.topic, value=message.encode('utf-8'))
        self.producer.flush()