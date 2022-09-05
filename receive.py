import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')     #create a queue, irrespective of send.py

    def callback(ch, method, properties, body):   #callback function is called by Pika library; to subscribe to the Publisher
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True) #tell rabbitmq to receive messages from 'hello' queue

    print(' [*] Waiting for messages. To exit press CTRL+C') #never-ending loop waiting for messages
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
