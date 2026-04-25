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



    """
versión 1.0.1
MEJORAS AL CÓDIGO
Manejo de errores en conexión (try/except)
Detecta cuando el servidor se desconecta (if not datos)
Permite salir escribiendo "salir"
Uso de daemon=True para que los hilos no bloqueen el cierre
Evita que el programa termine inmediatamente (loop final)
   """
import socket
import threading
import sys

IP_DESTINO = '127.0.0.1'  # Cambia por la IP real del servidor
PUERTO_DESTINO = 5000

try:
    sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_cliente.connect((IP_DESTINO, PUERTO_DESTINO))
    print(f"Conectado al servidor {IP_DESTINO}:{PUERTO_DESTINO}")
except Exception as e:
    print("Error al conectar:", e)
    sys.exit()

def escuchar_mensajes():
    while True:
        try:
            datos = sock_cliente.recv(1024)
            if not datos:
                print("Servidor desconectado")
                break
            print("\nMensaje recibido:", datos.decode('utf-8'))
        except Exception as e:
            print("Error al recibir:", e)
            break
    
    sock_cliente.close()
    sys.exit()

def enviar_mensajes():
    while True:
        try:
            texto = input()
            if texto.lower() == "salir":
                sock_cliente.close()
                print("Conexión cerrada")
                sys.exit()
            sock_cliente.send(texto.encode('utf-8'))
        except Exception as e:
            print("Error al enviar:", e)
            break

# Hilos
threading.Thread(target=escuchar_mensajes, daemon=True).start()
threading.Thread(target=enviar_mensajes, daemon=True).start()

# Mantener el programa vivo
while True:
    pass
