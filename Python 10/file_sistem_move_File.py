import os

# Ruta del archivo de origen (main.txt)
ruta_origen = "C:\Users\mzara\OneDrive\Documentos\BYJU\Python\Python 10\main.txt"

# Ruta del archivo de destino (nuevo_nombre.txt)
ruta_destino = "C:\Users\mzara\OneDrive\Documentos\BYJU\Python\Python 10\mario.txt"

# Usamos os.rename() para cambiar el nombre del archivo
try:
    os.rename(ruta_origen, ruta_destino)
    print(f"El archivo {ruta_origen} ha sido renombrado como {ruta_destino}")
except FileNotFoundError:
    print(f"El archivo {ruta_origen} no se encuentra en la ubicación especificada.")
except FileExistsError:
    print(f"Ya existe un archivo con el nombre {ruta_destino}.")
except Exception as e:
    print(f"Se produjo un error al intentar cambiar el nombre del archivo: {e}")