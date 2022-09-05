import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))     #establish connection with rabbitmq; connected to the broker on same machine i.e. local host
channel = connection.channel()

channel.queue_declare(queue='hello')        #create queue (if not, msg will be dropped) and name it 'hello'

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')     #routing key= queue name
print(" [x] Sent 'Hello World!'")
connection.close()
