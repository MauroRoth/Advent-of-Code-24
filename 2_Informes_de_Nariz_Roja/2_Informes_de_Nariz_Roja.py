#informes = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]
# Abre el archivo en modo lectura
try:
    with open("input.txt", "r") as archivo:
        # Lee todo el contenido del archivo en una cadena
        contenido = archivo.read()
        #print("Contenido completo:\n", contenido)
        archivo.seek(0)
        datos = [line.rstrip('\n').split(' ') for line in archivo]
except FileNotFoundError:
    print("Error: El archivo no se encuentra.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

informes = [[ int(nivel) for nivel in informe] for informe in datos]

def es_seguro(informe: list[int])->bool:
    nivel_primero = informe.pop(0)
    diferencias = list()
    for nivel in informe:
        diferencia = nivel - nivel_primero
        nivel_primero = nivel
        diferencias.append(diferencia)
    iguales = len(list(filter(lambda x: x==0, diferencias))) != 0
    mayores_tres = len(list(filter(lambda x: (x<-3 or x>3), diferencias))) != 0
    decrecientes = len(list(filter(lambda x: x<0, diferencias))) == len(diferencias)
    crecientes = len(list(filter(lambda x: x>0, diferencias))) == len(diferencias)
    condicion_general = (iguales or mayores_tres) or not(decrecientes or crecientes)
    return not condicion_general

seguro=0
inseguro=0
for informe in informes:
    #print(informe,end=' ')
    resultado = es_seguro(informe)
    #print(resultado)
    if resultado == True: seguro+=1
    if resultado == False: inseguro+=1
print("Informes Seguros: ", seguro)
print("Informes Inseguros: ", inseguro)



