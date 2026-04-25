# Decisiones del Proyecto

## Método elegido

Se utilizó conexión mediante hotspot.

## Justificación

Ventajas:

* Fácil de configurar
* No requiere router

Desventajas:

* Alcance limitado
* Dependencia de un dispositivo anfitrión

## Comandos usados

### Windows

```bash
netsh wlan set hostednetwork mode=allow ssid=MiRed key=12345678
netsh wlan start hostednetwork
```

### Linux

```bash
nmcli dev wifi hotspot
```

## Problemas encontrados

* Firewall bloqueando conexión → se solucionó permitiendo el puerto
* Error de IP → se verificó con ipconfig

## Soluciones

* Verificar IP correcta
* Revisar conexión Wi-Fi
* Abrir puertos necesarios

Hecho por: Elsy
