import pika
import time
import random
from argparse import ArgumentParser

class DistributedLock:
    def __init__(self, id):
        self.id = id
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.response = None 

        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
        self.queue_name = f'queue-{self.id}'
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.queue_bind(exchange='direct_logs', queue=self.queue_name, routing_key=self.id)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_response, auto_ack=False)

    def on_response(self, ch, method, props, body):
        if self.id == props.correlation_id:
            print(f"Response for this request, id: {self.id}")
            self.response = body
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def acquire_lock(self):
        self.response = None
        print("Lock requested")
        self.channel.basic_publish(
            exchange='direct_logs',
            routing_key='lock_manager',
            properties=pika.BasicProperties(
                correlation_id=self.id,
                delivery_mode=2,
            ),
            body='request_lock'
        )
        while self.response is None:
            print("Waiting for lock")
            self.connection.process_data_events()
            time.sleep(1)
        return self.response.decode('utf-8') == 'lock_granted'

    def release_lock(self):
        self.response = None
        print("Lock release requested")
        self.channel.basic_publish(
            exchange='direct_logs',
            routing_key='lock_manager',
            properties=pika.BasicProperties(
                correlation_id=self.id,
                delivery_mode=2,
            ),
            body='release_lock'
        )
        while self.response is None:
            print("Waiting for lock release")
            self.connection.process_data_events()
            time.sleep(1)
        return self.response.decode('utf-8') == 'lock_released'

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-i', '--id')
    args = parser.parse_args()
    lock = DistributedLock(args.id)
    requestTime = int(random.random()*10) + 5
    while True:
        time.sleep(requestTime)
        lock.acquire_lock()
        print("Lock acquired")
        time.sleep(2)
        lock.release_lock()
        print("Lock released")
