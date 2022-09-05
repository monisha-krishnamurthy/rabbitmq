import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"        #arbitratry messages will be sent from command line
channel.basic_publish(
    exchange='',
    routing_key='task_queue',          #adv of using 'task_queue' is the ability to easily parallelise work
    body=message,                      #alllocates messages in round-robin fashion
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE    #to mark Messages as durable so that they're not lost when RabbitMQ crashes
    ))
print(" [x] Sent %r" % message)
connection.close()
