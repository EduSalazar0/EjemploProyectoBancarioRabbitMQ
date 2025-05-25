from config.connection import get_connection
import json

def callback_log(ch, method, properties, body):
    transaccion = json.loads(body)
    print(f"[LOG] Cliente: {transaccion['cliente_id']} - Monto: ${transaccion['monto']} - Tipo: {transaccion['tipo']}")

def consumir_logs():
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue='logs.transacciones', durable=True)

    channel.basic_consume(
        queue='logs.transacciones',
        on_message_callback=callback_log,
        auto_ack=True
    )

    print("[*] Esperando logs de transacciones...")
    channel.start_consuming()

if __name__ == "__main__":
    consumir_logs()
