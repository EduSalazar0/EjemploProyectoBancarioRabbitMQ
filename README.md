
# Proyecto: Sistema Bancario con RabbitMQ

## Descripción General
Este proyecto simula un sistema bancario distribuido utilizando RabbitMQ como gestor de colas para manejar la comunicación asíncrona entre distintos servicios:
- **Productores** que emiten transacciones,
- **Consumidores** que procesan logs y detectan fraudes.

### Componentes Clave
- Exchange `dev.direct`: Para logs como "transaccion.depositar"
- Exchange `dev.topic`: Para patrones como "fraude.*"
- Colas: `logs.transacciones`, `seguridad.fraudes`

## Estructura del Proyecto
- `config/`: Conexión a RabbitMQ
- `producer/servicios/`: Simulación de operaciones como depósitos
- `consumer/logs/`: Registro de transacciones
- `consumer/fraudes/`: Revisión de fraudes
- `utils/`: Módulos de soporte (logging, etc.)
