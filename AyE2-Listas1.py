def MaxMin(operador):#Calcula el valor maximo o minimo segun la opcion seleccionada
    exec("evaluando = " + operador + "(elementos)")#Se ejecuta la cadena como una sentencia con el operador recibido
    return evaluando#Se regresa el numero maximo o minimo segun la opcion

def opcionMenu(opcion):#Recibe como parametro la opcion seleccionada
    if opcion == "1":#Calcular Maximo
        print "\nMaximo:", MaxMin("max")#Se llama a la funcion MaxMin y se pasa la funcion "max"
    elif opcion == "2":#Calcular Minimo
        print "\nMinimo:", MaxMin("min")#Se llama a la funcion MaxMin y se pasa la funcion "min"
    elif opcion == "3":#Salir
        exit()
    else:#Imprime error
        print "Opcion invalida\n"

elementos = []#Lista a crear
i = 1#Cantidad de numeros ingresados
nuevoItem = ""#Numero ingresado por el usuario leido como cadena
while (nuevoItem != "t"):#Se repetira este ciclo hasta que el usuario decida terminar la adicion de elementos ingresando "t"
    nuevoItem = raw_input("Numero " + str(i) + "(t para terminar): ")#Se lee el numero como cadena de texto
    if nuevoItem.isdigit():#Se revisa que el texto ingresado sea numero
        elementos.append(int(nuevoItem))#Se agrega a la lista
        i += 1#Se le suma 1 al contador de elementos
    elif nuevoItem != "t":#Si la cadena ingresada no es un numero pero tampoco es "t" se imprime error
        print "Numero Invalido"

while True:#Se repetira hasta que el usuario salga del programa
    print "Menu Principal\nLista:", elementos[:], "\n1.- Calcular Maximo\n2.- Calcular Minimo\n3.- Salir"
    opcion = raw_input("Opcion: ")#Lee la opcion selecionada
    opcionMenu(opcion)