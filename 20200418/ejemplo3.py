# definir un diccionario vacio
diccionario = {} 

# definir un diccionario con elementos
diccionario = {'Julio': 123456, 'Jorge': 654321} 

# modificar un valor
diccionario['Julio'] = 1234567

# agregar una llave:valor
diccionario['Saida'] = 987654

# consultar un valor segun una llave leida del teclado
try:
    llave = input("Ingrese una llave: ")
    print(diccionario[llave])
except KeyError:
    print("No se encontro la llave en el diccionario.")

# mostrar todos los elementos del diccionario
for llave, valor in diccionario.items():
    print(llave, "->", valor)

# mostrar todas las llaves del diccionario
print("-------------------")
print("Llaves del diccionario")
for llave in diccionario.keys():
    print(llave)

# mostrar todos los valores
print("-------------------")
print("Valores del diccionario")
for valor in diccionario.values():
    print(valor)