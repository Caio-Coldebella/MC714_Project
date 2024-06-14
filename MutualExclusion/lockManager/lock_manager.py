import pika
from collections import deque

def lock_manager():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='lock_queue')
    current_lock_holder = None
    lock_queue = deque()

    def on_request(ch, method, props, body):
        nonlocal current_lock_holder
        if body.decode('utf-8') == 'request_lock':
            print("Lock requested")
            print(props)
            if current_lock_holder is None:
                current_lock_holder = props.reply_to
                ch.basic_publish(
                    exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id=props.correlation_id),
                    body='lock_granted'
                )
            else:
                lock_queue.append((props.reply_to, props.correlation_id))
                
        elif body.decode('utf-8') == 'release_lock':
            print("Lock released")
            current_lock_holder = None
            if lock_queue:
                next_lock_holder, corr_id = lock_queue.popleft()
                current_lock_holder = next_lock_holder
                ch.basic_publish(
                    exchange='',
                    routing_key=next_lock_holder,
                    properties=pika.BasicProperties(correlation_id=corr_id),
                    body='lock_granted'
                )

    channel.basic_consume(queue='lock_queue', on_message_callback=on_request, auto_ack=True)
    print("Lock manager started")
    channel.start_consuming()

if __name__ == "__main__":
    lock_manager()