# Haga un procedimiento (input nombre del archivo)
# que lea todas las lineas de un archivo
# y las despliegue en pantalla convirtiendo el texto a mayusculas.
def desplegarFileMayusculas(archivo):
    try:
        archivo_entrada = open(archivo)
        texto = archivo_entrada.read()
        texto = texto.upper()  # convierto a mayusculas
        print(texto)
        archivo_entrada.close()
    except FileNotFoundError:
        print("Archivo", archivo, "no encontrado")

#Haga un programa principal que lea el nombre del archivo del teclado
# y usando el procedimiento anterior me despliegue el archivo
def main():
    nombre_archivo = input("Ingrese un nombre de archivo: ")
    desplegarFileMayusculas(nombre_archivo)

main()