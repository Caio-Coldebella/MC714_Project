import pika
import uuid
import time
import random

class DistributedLock:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.callback_queue = None
        self.lock_queue = 'lock_queue'

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def acquire_lock(self):
        if(self.callback_queue is None):
            self.callback_queue = self.channel.queue_declare(queue='lock_queue').method.queue
        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_response, auto_ack=True)
        self.channel.basic_publish(
            exchange='',
            routing_key=self.lock_queue,
            properties=pika.BasicProperties(reply_to=self.callback_queue, correlation_id=self.corr_id),
            body='request_lock'
        )
        while self.response is None:
            self.connection.process_data_events()
        return self.response.decode('utf-8') == 'lock_granted'

    def release_lock(self):
        self.response = None

        
        self.channel.basic_publish(
            exchange='',
            routing_key=self.lock_queue,
            body='release_lock'
        )

if __name__ == "__main__":
    lock = DistributedLock()
    requestTime = int(random.random()*30) + 5
    while True:
        time.sleep(requestTime)
        lock.acquire_lock()
        time.sleep(2)
        lock.release_lock()
