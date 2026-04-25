import socket
import threading

IP_SERVIDOR = '0.0.0.0'
PUERTO_SERVIDOR = 5000

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind((IP_SERVIDOR, PUERTO_SERVIDOR))
sock_server.listen()

lista_conexiones = []

def atender_usuario(conexion, direccion):
    print(f"[CONECTADO] Cliente {direccion}")

    while True:
        try:
            datos = conexion.recv(1024).decode('utf-8')
            if not datos:
                break

            print(f"{direccion} -> {datos}")

            # Enviar a los demás clientes
            for usuario in lista_conexiones:
                if usuario != conexion:
                    usuario.send(datos.encode('utf-8'))

        except:
            break

    print(f"[SALIDA] Cliente {direccion}")
    lista_conexiones.remove(conexion)
    conexion.close()

print("Servidor en espera de conexiones...")

while True:
    conexion, direccion = sock_server.accept()
    lista_conexiones.append(conexion)

    hilo = threading.Thread(target=atender_usuario, args=(conexion, direccion))
    hilo.start()


#versión mejorada y más robusta por Dante
"Manejo correcto de errores"
"Cierre limpio de conexiones"
"Identificación de clientes"
"Evitar fallos si un cliente se desconecta mal"

import socket
import threading

IP_SERVIDOR = '0.0.0.0'
PUERTO_SERVIDOR = 5000

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind((IP_SERVIDOR, PUERTO_SERVIDOR))
sock_server.listen(5)

clientes = []

def broadcast(mensaje, origen):
    """Envía mensaje a todos menos al que lo envió"""
    for cliente in clientes:
        if cliente != origen:
            try:
                cliente.send(mensaje)
            except:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def atender_cliente(conexion, direccion):
    print(f"[CONECTADO] {direccion}")

    try:
        while True:
            datos = conexion.recv(1024)

            if not datos:
                break

            mensaje = datos.decode('utf-8')
            print(f"{direccion}: {mensaje}")

            broadcast(datos, conexion)

    except Exception as e:
        print(f"[ERROR] {direccion}: {e}")

    finally:
        print(f"[DESCONECTADO] {direccion}")
        if conexion in clientes:
            clientes.remove(conexion)
        conexion.close()

print(f"[SERVIDOR] Escuchando en {IP_SERVIDOR}:{PUERTO_SERVIDOR}")

while True:
    conexion, direccion = sock_server.accept()
    clientes.append(conexion)

    hilo = threading.Thread(target=atender_cliente, args=(conexion, direccion))
    hilo.daemon = True
    hilo.start()
