import pika

def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            virtual_host='dev',
            credentials=pika.PlainCredentials('guest', 'guest')
        )
    )



