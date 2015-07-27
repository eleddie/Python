def imprimirMenu():
    print("Menu Principal:\n1.- Convertir\n2.- Salir\n")

def opcionSeleccionada(opcion):
    if opcion == '1':#Convertir
        numeroAConvertir = raw_input("Insertar numero a convertir: ")
        if numeroAConvertir.isdigit():
            print("El numero " + numeroAConvertir + " en binario es: " + bin(int(numeroAConvertir))[2:] + "\n")
            print("El numero " + numeroAConvertir + " en octal es: " + oct(int(numeroAConvertir))[1:] + "\n")
            print("El numero " + numeroAConvertir + " en hexadecimal es: " + hex(int(numeroAConvertir))[2:] + "\n")
        else:
            print("Numero Invalido")
    elif opcion == '2':#Salir
        exit()
    else:#Opcion Incorrecta
        print("Opcion Incorrecta\n\n")

while (True):
    imprimirMenu()
    opcion = raw_input("Insertar Opcion: ")
    opcionSeleccionada(opcion)
