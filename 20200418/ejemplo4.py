
# definimos nuestro diccionario para guardar los numeros
agenda = {}

# Listado de la agenda:
#   Jorge: [12345678, 87654321]
#   Camila: [12345678, 87654321]
def listar_agenda():
    print("Listado de la agenda:")
    for k, v in agenda.items():
        print("\t", k, ":", str(v)) 

def agregar_numero():
    nombre = input("Ingrese el nombre: ")
    numero = int(input("Ingrese un numero: "))
    try:
        if numero in agenda[nombre]:
            print("No se agrego el numero por que ya existia!")
        else:
            agenda[nombre].append(numero)
            print("Contacto existente actualizado")
    except KeyError:
        agenda[nombre] = [numero]
        print("Nuevo contacto agregado exitosamente")

def eliminar_persona():
    nombre = input("Ingrese el nombre: ")
    try:
        del agenda[nombre]
        print("Contacto eliminado existosamente")
    except KeyError:
        print("Error: no se elimino por que no existe ese contacto")

def main():
    while True:
        try:
            print("\n1. Listar Agenda.")
            print("2. Agregar un numero.")
            print("3. Eliminar una persona.")
            print("4. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                listar_agenda()
            elif opcion == 2:
                agregar_numero()
            elif opcion == 3:
                eliminar_persona()
            elif opcion == 4:
                break
            else:
                print("Error: opcion ingresada invalida")
        except ValueError:
            print("Error: opcion ingresada invalida")
main()