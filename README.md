
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
# 💰 Proyecto: Sistema Bancario Distribuido con RabbitMQ

---

## 📌 Descripción General

Este proyecto representa la simulación de un **sistema bancario distribuido**, en el que los distintos componentes de la arquitectura interactúan mediante una solución de **mensajería asíncrona basada en RabbitMQ**. El objetivo es gestionar transacciones bancarias y procesos críticos como auditoría, validación de usuarios y detección de fraudes, todo ello desacoplado y bajo una lógica de microservicios.

El sistema está diseñado con principios de **alta disponibilidad, escalabilidad y trazabilidad**, empleando colas de mensajes y exchanges específicos para enrutar eventos financieros de forma confiable.

---

## 🧩 Componentes Clave

- 🔁 **Exchange `dev.direct`:** Encargado de enrutar eventos directos como:
  - `transaccion.depositar`
  - `transaccion.retirar`
  - `transaccion.transferir`

- 🧠 **Exchange `dev.topic`:** Diseñado para patrones flexibles, tales como:
  - `fraude.*` → eventos de seguridad
  - `validacion.*` → eventos de control de identidad

- 📦 **Colas configuradas:**
  - `logs.transacciones`
  - `seguridad.fraudes`
  - `notificaciones`
  - `auditoria.transacciones`
  - `validacion.usuario`

Estas colas reciben los mensajes según las reglas de ruteo definidas en el archivo `definitions.json`.

---

## 🏗️ Estructura del Proyecto

