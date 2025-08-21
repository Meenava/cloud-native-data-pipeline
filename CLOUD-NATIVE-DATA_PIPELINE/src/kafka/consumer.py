class KafkaConsumer:
    def __init__(self, kafka_config):
        from kafka import KafkaConsumer
        self.consumer = KafkaConsumer(
            kafka_config['topic'],
            bootstrap_servers=kafka_config['bootstrap_servers'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=kafka_config['group_id']
        )

    def consume_messages(self, topic):
        self.consumer.subscribe([topic])
        for message in self.consumer:
            print(f"Consumed message: {message.value.decode('utf-8')} from topic: {topic}")