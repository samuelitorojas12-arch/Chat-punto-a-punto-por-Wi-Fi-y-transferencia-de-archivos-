import socket
import threading

IP_DESTINO = 'IP_DEL_SERVIDOR'
PUERTO_DESTINO = 5000

sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_cliente.connect((IP_DESTINO, PUERTO_DESTINO))

def escuchar_mensajes():
    while True:
        try:
            datos = sock_cliente.recv(1024).decode('utf-8')
            print("\nMensaje recibido:", datos)
        except:
            print("Conexión perdida")
            sock_cliente.close()
            break

def enviar_mensajes():
    while True:
        texto = input()
        sock_cliente.send(texto.encode('utf-8'))

threading.Thread(target=escuchar_mensajes).start()
threading.Thread(target=enviar_mensajes).start()
