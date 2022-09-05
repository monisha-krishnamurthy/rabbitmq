#WORK QUEUE PROGRAM: used to distribute time consuming tasks among multiple workers by running many workers
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)   #When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to.
print(' [*] Waiting for messages. To exit press CTRL+C')   #Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))           #function used to fake a resource intensive task
    print(" [x] Done")                       #No. of dots denotes complexity
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)    #manual message acknowledgments; wait for ack before dispatching new msg

channel.start_consuming()