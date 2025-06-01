from config.connection import get_connection
import json

def callback(ch, method, properties, body):
    msg = json.loads(body)
    print(f"[NOTIFICACIÓN] {msg['mensaje']}")

def consumir():
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue='notificaciones', durable=True)

    channel.basic_consume(
        queue='notificaciones',
        on_message_callback=callback,
        auto_ack=True
    )

    print("[*] Esperando notificaciones...")
    channel.start_consuming()

if __name__ == "__main__":
    consumir()
