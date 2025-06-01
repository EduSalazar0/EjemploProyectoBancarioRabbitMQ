import pika

def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host='rabbitmq',
            port=5672,
            virtual_host='dev',
            credentials=pika.PlainCredentials('admin', 'admin123')
        )
    )
