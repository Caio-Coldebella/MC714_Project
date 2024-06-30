import pika
import time

class lock_manager():
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.current_lock_holder = None
        self.start()

    def start(self):
        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
        self.channel.queue_declare(queue='lock_manager', durable=True)
        self.channel.queue_bind(exchange='direct_logs', queue='lock_manager', routing_key='lock_manager')
        self.channel.basic_consume(queue='lock_manager', on_message_callback=self.on_request, auto_ack=False)

        print("Lock manager started")
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        if body.decode('utf-8') == 'request_lock':
            print(f"Lock requested by {props.correlation_id}")
            if self.current_lock_holder is None:
                print(f"Lock granted to {props.correlation_id}")
                self.current_lock_holder = props.correlation_id
                ch.basic_publish(
                    exchange='direct_logs',
                    routing_key=props.correlation_id,
                    properties=pika.BasicProperties(
                        correlation_id=props.correlation_id
                    ),
                    body='lock_granted'
                )
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                print(f"Lock denied to {props.correlation_id} as it is held by {self.current_lock_holder}")
                time.sleep(1)
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
                
        elif body.decode('utf-8') == 'release_lock':
            print(f"Lock released by {props.correlation_id}")
            ch.basic_publish(
                exchange='direct_logs',
                routing_key=props.correlation_id,
                properties=pika.BasicProperties(
                    correlation_id=props.correlation_id
                ),
                body='lock_released'
            )
            self.current_lock_holder = None
            ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    manager = lock_manager()