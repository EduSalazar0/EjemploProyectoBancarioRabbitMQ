from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure_bus.config.azure_config import AzureServiceBusConfig

import time

def send_transaction():
    client = ServiceBusClient.from_connection_string(conn_str=AzureServiceBusConfig.CONNECTION_STR, logging_enable=True)
    with client:
        sender = client.get_queue_sender(queue_name=AzureServiceBusConfig.QUEUE_NAME)
        with sender:
            for i in range(1, 11):
                message = ServiceBusMessage(f"Transferencia #{i}: $500 de la cuenta 123 a 456.")
                sender.send_messages(message)
                print(f"Mensaje {i} enviado.")
                time.sleep(0.5)  # Pequeña pausa para visualización

if __name__ == "__main__":
    send_transaction()
