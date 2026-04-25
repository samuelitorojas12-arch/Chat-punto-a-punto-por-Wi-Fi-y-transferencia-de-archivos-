# Teoría de Redes y Sockets

## ¿Qué es un socket?

Un socket es un punto de comunicación entre dos dispositivos en una red. Permite enviar y recibir datos entre aplicaciones mediante protocolos como TCP o UDP.

Ejemplo: un cliente se conecta a un servidor mediante IP y puerto.

## TCP vs UDP

| Característica | TCP       | UDP        |
| -------------- | --------- | ---------- |
| Conexión       | Sí        | No         |
| Confiabilidad  | Alta      | Baja       |
| Velocidad      | Más lento | Más rápido |

TCP se usa cuando se requiere confiabilidad (chat).
UDP se usa cuando importa más la velocidad (streaming).

## Puertos e IP

* IP: identifica un dispositivo en la red
* Puerto: identifica una aplicación

Ejemplo: 192.168.1.5:5000

## NAT

El NAT permite que varios dispositivos compartan una misma IP pública, pero puede dificultar conexiones entre redes distintas.

## Firewalls

Protegen la red bloqueando puertos. Es necesario permitir el puerto usado por el chat.

## Tipos de conexión Wi-Fi

* Misma red: ambos dispositivos conectados al mismo router
* Hotspot: uno crea red y el otro se conecta
* Wi-Fi Direct: conexión directa entre dispositivos

## Seguridad

La comunicación en este proyecto es en texto plano. Para mayor seguridad se recomienda usar TLS/SSL.


