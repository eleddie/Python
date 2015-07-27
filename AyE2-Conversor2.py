def opcionSeleccionada(opcion):#Recibe como parametro la opcion
    if opcion == '1':#Convertir
        numeroAConvertir = raw_input("Insertar numero a convertir: ")#Lee el numero a convertir como cadena de texto
        if numeroAConvertir.isdigit(): #Revisa si la cadena ingresada es un numero e imprime el resultado
            print("El numero " + numeroAConvertir + " en binario es: " + conversion(int(numeroAConvertir),2) + "\n")
            print("El numero " + numeroAConvertir + " en octal es: " + conversion(int(numeroAConvertir),8) + "\n")
            print("El numero " + numeroAConvertir + " en hexadecimal es: " + conversion(int(numeroAConvertir),16) + "\n")
        else: #Si el texto ingresado no es numero imprime error y regresa al menu
            print("Numero Invalido")
    elif opcion == '2':#Salir
        exit()
    else:#Opcion Incorrecta
        print("Opcion Incorrecta\n\n")
        
def conversion(numero, base):#Recibe como parametro el numero a convertir y la base del sistema numerico
    numConvertido = ""#Inicializa una variable para almacenar los residuos
    while numero >= base:#Divide el numero hasta que sea menor que la base
        if numero % base >= 10:#Si el residuo es mayor a 10
            numConvertido = str(chr(numero%base-10 + ord("A"))) + numConvertido#Se le agrega la letra correspondiente
        else:#Si el residuo es menor a 10, se coloca el resultado
            numConvertido = str(numero % base) + numConvertido
        numero = numero / base#Por cada vuelta se divide el numero entre la base (Division Entera)
    numConvertido = str(numero) + numConvertido#Al salir del ciclo while se anade el numero que queda
    return numConvertido#Se regresa el numero convertido

while (True):#Se repite hasta que se decida salir
    print("Menu Principal:\n1.- Convertir\n2.- Salir\n")
    opcion = raw_input("Insertar Opcion: ")#Se lee la opcion
    opcionSeleccionada(opcion)#Se llama el metodo pasandole la opcion
