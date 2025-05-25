from config.connection import get_connection
import json
import time

def emitir_deposito(cliente_id, monto):
    connection = get_connection()
    channel = connection.channel()

    transaccion = {
        "cliente_id": cliente_id,
        "monto": monto,
        "tipo": "deposito",
        "timestamp": time.time()
    }

    channel.basic_publish(
        exchange='dev.direct',
        routing_key='transaccion.depositar',
        body=json.dumps(transaccion)
    )

    if monto > 10000:
        channel.basic_publish(
            exchange='dev.topic',
            routing_key='fraude.deposito',
            body=json.dumps(transaccion)
        )

    print(f"Transacción emitida: {transaccion}")
    connection.close()

if __name__ == "__main__":
    emitir_deposito("CL123", 15000)
