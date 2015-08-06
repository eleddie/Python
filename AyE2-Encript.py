semilla = ""#Se inicializa la semilla vacia
def cambiarSemilla():
    global semilla#Se utiliza la variable global
    semilla = raw_input("Introducir semilla: ")#Lee la semilla
    if semilla == "":#Si esta vacia se toma como un espacio
        semilla = " "
    semilla = ord(semilla[0]) % 4 + 4#Obtiene el valor numerico del primer caracter de la semilla insertada y le suma 4 al residuo de la division entre 4(Rango de 4 valores)

def encriptar(frase, indice, encriptado, semilla):#Recibe como parametro la frase a encriptar, el primer indice, la frase encriptada hasta el momento y la semilla
    if indice >= len(frase):#Caso base. Si ya recorrio todos los caracteres, regresa la cadena encriptada
        return encriptado
    else:#Parte Recursiva. Anade a la variable encriptado el caracter nuevo(encriptado)
        #Convierte el caracter en la posicion "indice" en dos caracteres, el primero es el primer digito del equivalente decimal del caracter por 10 mas la semilla-1
        #Y el segundo es la semilla+1 por 10 mas el segundo digito del equivalente decimal del caracter
        encriptado += chr((ord(frase[indice])/10)*10+(semilla-1)) + chr((ord(frase[indice])%10)+10*(semilla+1))
        if semilla == 7:#Si la semilla es 7 regresa a 3 para que no de errores con letras minusculas
            semilla = 3
        #Se vuelve a llamar pasando la frase igual, el indice+1, la nueva variable "encriptado" y la semilla+1 para que siempre sea diferente
        return encriptar(frase, indice+1, encriptado, semilla+1)

def desencriptar(frase, indice, desencriptado):#Recibe como parametro la frase a encriptar, el primer indice y la frase desencriptada hasta el momento
    if indice >= len(frase)-1:#Caso base. Si ya recorrio todos los caracteres, regresa la cadena desencriptada
        return desencriptado
    else:#Parte Recursiva. Anade a la variable desencriptado el caracter nuevo(desencriptado)
        #Agarra los dos siguientes caracteres de "frase", del primero se obtiene el primer digito del equivalente decimal y se multiplica por 10
        #Y del segundo se obtiene el ultimo digito del equivalente decimal del caracter, luego se suma y se obtiene el character equivalente al decimal
        desencriptado += chr((ord(frase[indice])/10)*10 + ord(frase[indice+1])%10)
        return desencriptar(frase, indice+2, desencriptado)#Se vuelve a llamar pasando la frase igual, el indice+2 y la nueva variable "desencriptado"

def opcionMenu(opcion):#Opciones del menu
    if opcion == "1":#Encriptar una palabra
        global semilla#Se utiliza la variable global
        fraseAEncriptar = raw_input("Insertar frase a encriptar: ")#Lee la palabra
        if len(fraseAEncriptar) == 0:#Si la frase ingresada esta vacia muestra error y regresa al menu
            print "Frase vacia"
        else:
            print "La frase encriptada equivale a: " + encriptar(fraseAEncriptar.upper(),0,"",semilla), "\n"#Llama a la funcion e imprime el resultado
    elif opcion == "2":#Desencriptar una palabra
        fraseADesencriptar = raw_input("Insertar frase a desencriptar: ")#Lee el codigo a desencriptar
        if len(fraseADesencriptar) == 0:#Si el codigo ingresado esta vacio muestra error y regresa al menu
            print "Codigo vacio"
        else:
            print "El codigo desencriptado equivale a: " + desencriptar(fraseADesencriptar.upper(),0,""), "\n"#Llama a la funcion e imprime el resultado
    elif opcion == "3":#Cambiar la semilla
       print ""
       cambiarSemilla()
    elif opcion == "4":#Salir
        exit()
    else:#Opcion invalida
        print "Opcion Invalida\n"

cambiarSemilla()
while True:#Se repetira hasta que el usuario decida salir
    print("Menu Principal:\n1.- Encriptar Frase\n2.- Desencriptar\n3.- Cambiar Semilla\n4.- Salir")#Imprime el menu
    opcion = raw_input("Opcion: ")#Lee la opcion
    opcionMenu(opcion)#Se llama la funcion de opciones del menu pasandole la opcion seleccionada
