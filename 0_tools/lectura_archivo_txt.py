# Abre el archivo en modo lectura
try:
    with open("mi_archivo.txt", "r") as archivo:
        # Lee todo el contenido del archivo en una cadena
        contenido = archivo.read()
        print("Contenido completo:\n", contenido)

        # Lee el archivo línea por línea
        archivo.seek(0)  # Regresa al inicio del archivo
        lineas = archivo.readlines()
        print("\nLíneas individuales:\n", lineas)

        # Lee una sola línea
        archivo.seek(0)
        primera_linea = archivo.readline()
        print("\nPrimera línea:\n", primera_linea)
except FileNotFoundError:
    print("Error: El archivo no se encuentra.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
