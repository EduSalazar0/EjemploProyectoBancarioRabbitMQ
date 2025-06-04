from azure.servicebus import ServiceBusClient
from azure_bus.config.azure_config import AzureServiceBusConfig

def receive_transaction():
    client = ServiceBusClient.from_connection_string(conn_str=AzureServiceBusConfig.CONNECTION_STR, logging_enable=True)
    with client:
        receiver = client.get_queue_receiver(queue_name=AzureServiceBusConfig.QUEUE_NAME)
        with receiver:
            received_count = 0
            for msg in receiver.receive_messages(max_wait_time=5, max_message_count=10):
                print("Mensaje recibido:", str(msg))
                receiver.complete_message(msg)
                received_count += 1
            print(f"Total de mensajes recibidos: {received_count}")

if __name__ == "__main__":
    receive_transaction()





