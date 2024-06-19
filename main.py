# Práctica de Listas doblemente enlazadas de la clase 5
from ListaDoble import ListaDobleEnlazada

lista = ListaDobleEnlazada()
numero = 0
opcion = 0

while opcion !=7:
    opcion= int(input("Digite la opcion que requiera: \n"
                      "1. ingresar al final\n"
                      "2. ingresar al inicio\n"
                      "3. Mostrar \n"
                      "4. Buscar \n"
                      "5. Modificar \n"
                      "6. Eliminar \n"
                      "7. Salir \n: "))
    match opcion:
        case 1:
            numero= int(input("Digite el número que desea insertar: "))
            lista.agregar_final(numero)
        case 2:
            numero= int(input("Digite el número que desea insertar: "))
            lista.agregar_inicio(numero)
        case 3:
            lista.mostrar()
        case 4:
            numero=int(input("Digite el número que desea buscar: "))
            if lista.buscar(numero):
                print("El número se encuentra en la lista")
            else:
                print("El número NO se encuentra en la lista")
        case 5:
            datoActual=int(input("Digite el número que desea modificar: "))
            datoNuevo=int(input("Digite el nuevo número con el que lo desea cambiar: "))
            lista.modificar(datoActual,datoNuevo)
        case 6:
            numero= int(input("Digite el número que desea eliminar: "))
            lista.eliminar(numero)
        case 7:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")