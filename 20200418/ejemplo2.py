def getLinesOfFile(file):
    try:
        input_file = open(file)
        lista = []
        for line in input_file:
            lista.append(line.upper().strip("\n"))
        input_file.close()
        return lista
    except FileNotFoundError:
        return []

# haga un procedimiento que reciba una lista y escriba a un archivo
# todos los elementos de la lista colocando un elemento por linea.
# Los inputs seran el nombre del archivo y la lista.
def writeListToFile(file, lista):
    archivo = open(file, "w")
    for element in lista:
        archivo.write(element + "\n")
    archivo.close()

#Haga un programa principal que lea el nombre del archivo del teclado
# y usando el procedimiento anterior me despliegue el archivo
def main():
    nombre_archivo_in = input("Ingrese un nombre de archivo entrada: ")
    lista = getLinesOfFile(nombre_archivo_in)
    nombre_archivo_out = input("Ingrese un nombre de archivo salida: ")
    writeListToFile(nombre_archivo_out, lista)

main()