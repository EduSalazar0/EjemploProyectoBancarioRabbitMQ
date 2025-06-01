from config.connection import get_connection
import json

def callback(ch, method, properties, body):
    evento = json.loads(body)
    print(f"[AUDITORÍA] Evento registrado: {evento}")

def consumir():
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue='auditoria.transacciones', durable=True)

    channel.basic_consume(
        queue='auditoria.transacciones',
        on_message_callback=callback,
        auto_ack=True
    )

    print("[*] Esperando eventos para auditoría...")
    channel.start_consuming()

if __name__ == "__main__":
    consumir()
