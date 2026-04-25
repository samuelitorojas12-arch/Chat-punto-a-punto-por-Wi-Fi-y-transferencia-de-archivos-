import hashlib

def calculate_sha256(file_path):
sha256 = hashlib.sha256()
with open(file_path, "rb") as f:
for block in iter(lambda: f.read(4096), b""):
sha256.update(block)
return sha256.hexdigest()
Hecho por: Elsy

"version corregida y mejorada por Dante

import hashlib

def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    try:
        with open(ruta_archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha256.update(bloque)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: archivo no encontrado")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None
