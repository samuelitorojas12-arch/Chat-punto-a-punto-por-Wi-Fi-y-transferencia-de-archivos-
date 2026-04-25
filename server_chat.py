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
