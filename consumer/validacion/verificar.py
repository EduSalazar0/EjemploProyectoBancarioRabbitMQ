from config.connection import get_connection
import json

def callback(ch, method, properties, body):
    datos = json.loads(body)
    cuenta_valida = datos["cliente_id"].startswith("CL")
    print(f"[VALIDACIÓN] Cuenta {datos['cliente_id']} válida: {cuenta_valida}")

def consumir():
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue='validacion.usuario', durable=True)

    channel.basic_consume(
        queue='validacion.usuario',
        on_message_callback=callback,
        auto_ack=True
    )

    print("[*] Esperando solicitudes de validación...")
    channel.start_consuming()

if __name__ == "__main__":
    consumir()
