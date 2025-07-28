# Abre el archivo en modo lectura
try:
    with open("input.txt", "r") as archivo:
        # Lee todo el contenido del archivo en una cadena
        contenido = archivo.read()
        #print("Contenido completo:\n", contenido)
        archivo.seek(0)
        datos = [line.rstrip('\n').split('   ') for line in archivo]
except FileNotFoundError:
    print("Error: El archivo no se encuentra.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

lista1_input = [int(pares[0]) for pares in datos]
lista2_input = [int(pares[1]) for pares in datos]
lista1_ej = [3,4,2,1,3,3]
lista2_ej = [4,3,5,3,9,3]

lista1 = lista1_input
lista2 = lista2_input

lista1.sort()
lista2.sort()

print('Primera Parte')
distancia =list(map(lambda x,y: ((x-y)**2)**.5,lista1,lista2)) 
suma = sum(distancia)
print("SUMA DE DISTANCIAS: ",suma)

print('Segunda Parte')
puntajeT=0
for elemento in lista1:
    repeticiones = lista2.count(elemento) 
    puntaje = elemento*repeticiones
    puntajeT += puntaje
print('PUNTAJE DE SIMILITUD FINAL: ',puntajeT)
