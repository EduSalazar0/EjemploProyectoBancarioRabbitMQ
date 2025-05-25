from config.connection import get_connection
import json

def callback_fraude(ch, method, properties, body):
    transaccion = json.loads(body)
    print(f"[ALERTA FRAUDE] Cuenta: {transaccion['cliente_id']} - Monto: ${transaccion['monto']}")

def monitorear_fraudes():
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue='seguridad.fraudes', durable=True)

    channel.basic_consume(
        queue='seguridad.fraudes',
        on_message_callback=callback_fraude,
        auto_ack=True
    )

    print("[*] Monitoreando transacciones sospechosas...")
    channel.start_consuming()

if __name__ == "__main__":
    monitorear_fraudes()
