import pika

class lock_manager():
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='lock_queue')
        self.current_lock_holder = None
        self.start()

    def start(self):
        self.channel.basic_consume(queue='lock_queue', on_message_callback=self.on_request, auto_ack=True)
        print("Lock manager started")
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        if body.decode('utf-8') == 'request_lock':
            print("Lock requested")
            if self.current_lock_holder is None:
                print("Lock granted")
                self.current_lock_holder = props.reply_to
                ch.basic_publish(
                    exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id=props.correlation_id),
                    body='lock_granted'
                )
            else:
                print("Lock denied")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
                
        elif body.decode('utf-8') == 'release_lock':
            print("Lock released")
            ch.basic_publish(
                exchange='',
                routing_key=props.reply_to,
                properties=pika.BasicProperties(correlation_id=props.correlation_id),
                body='lock_released'
            )
            self.current_lock_holder = None

if __name__ == "__main__":
    manager = lock_manager()