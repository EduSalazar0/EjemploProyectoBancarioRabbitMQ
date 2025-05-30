from config.connection import get_connection
import pika
import json
import time

def emitir_deposito(cliente_id, monto):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange='dev.direct', exchange_type='direct', durable=True)

    mensaje = {
        "cliente_id": cliente_id,
        "monto": monto,
        "tipo": "deposito"
    }

    channel.basic_publish(
        exchange='dev.direct',
        routing_key='transaccion.depositar',
        body=json.dumps(mensaje),
        properties=pika.BasicProperties(delivery_mode=2)
    )

    print(f"[x] Enviado depósito: {mensaje}")
    connection.close()

if __name__ == "__main__":
    for i in range(10):
        emitir_deposito(f"CL123_{i}", 1000 * (i + 1))
        time.sleep(1)  # Espera de 1 segundo entre cada envío
