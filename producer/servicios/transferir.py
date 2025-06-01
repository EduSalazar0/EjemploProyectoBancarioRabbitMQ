from config.connection import get_connection
import pika
import json
import time

def emitir_transferencia(cliente_origen, cliente_destino, monto):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange='dev.direct', exchange_type='direct', durable=True)

    mensaje = {
        "cliente_origen": cliente_origen,
        "cliente_destino": cliente_destino,
        "monto": monto,
        "tipo": "transferencia"
    }

    channel.basic_publish(
        exchange='dev.direct',
        routing_key='transaccion.transferir',
        body=json.dumps(mensaje),
        properties=pika.BasicProperties(delivery_mode=2)
    )

    print(f"[x] Enviada transferencia: {mensaje}")
    connection.close()

if __name__ == "__main__":
    for i in range(10):
        emitir_transferencia(f"CL{i}01", f"CL{i}99", 1000 * (i + 1))
        time.sleep(1)
