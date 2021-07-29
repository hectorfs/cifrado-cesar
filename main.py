import sys #importo lib sys para poder leer los parametros de linea de comandos
abcdario = "abcdefghijklmnñopqrstuvwxyz" #defino los caracteres a evaluar

def cifrar(texto, rotacion): #defino funcion "cifrar"

    text_cifrado = "" #defino la salida vacia para ir agregando por caracter cifrado

    for letra in texto: #recorro el texto de entrada por caracter
        idxLetra = abcdario.find(letra) #obtengo el indice del caracter a cifrar (dentro del "abecedario")
        
        if idxLetra >= 0:   #si pertenece al abecedario opero, 
                            #no se tienen en cuenta caracteres especiales, ni numeros o espacios
                            #estos se dejan intactos
            idxLetra += rotacion #agrego la rotacion a la posicion encontrada

            if idxLetra >= len(abcdario): #caso fix, si excede 27 (caracteres del abecedario 0-26) queda fuera de rango
                idxLetra -= len(abcdario) #entonces procedo a restarle los 27 del "abcdario"

            text_cifrado = text_cifrado + str(abcdario[idxLetra]) #agrego al string de salida el nuevo caractec con la rotacion
        else:
            text_cifrado = text_cifrado + letra #dejo intacto lo que no este en "abcdario"

    return text_cifrado #retorno el texto completo cifrado

def decifrar(texto, rotacion): #defino funcion "descifrar"

    text_cifrado = "" #defino la salida vacia para ir agregando por caracter cifrado

    for letra in texto: #recorro el texto de entrada por caracter
        idxLetra = abcdario.find(letra) #obtengo el indice del caracter a cifrar (dentro del "abecedario")
        
        if idxLetra >= 0:   #si pertenece al abecedario opero, 
                            #no se tienen en cuenta caracteres especiales, ni numeros o espacios
                            #estos se dejan intactos
            idxLetra -= rotacion #resto la rotacion a la posicion encontrada
            text_cifrado = text_cifrado + str(abcdario[idxLetra]) #agrego al string de salida el nuevo caractec con la rotacion
        else:
            text_cifrado = text_cifrado + letra #dejo intacto lo que no este en "abcdario"

    return text_cifrado #retorno el texto completo cifrado

def main():
    if len(sys.argv) == 4: #evaluo la cantidad de parametros 3 + 1 el nombre del archivo idx 0
        funcion = sys.argv[1] #leo la funcion a realizar de los parametros de linea de comandos
        texto = sys.argv[2].lower() #leo el texto pasado como parametros de linea de comandos
        rotacion = int(sys.argv[3]) #leo la rotacion de los parametros de linea de comandos

        if rotacion > 26: #para evitar exceder el rango de busqueda en "abcdario" limito a 26 rotaciones
            print("Solo se permiten 26 rotaciones, has ingresado:", rotacion)
            return #dejo de ejecutar

        print("Texto a procesar (lower case): '",texto,"'") #imprimo texto a operar

        if funcion.lower() == "c": #si es C voy a cifrar
            print(cifrar(texto, rotacion)) #invoco metodo "cifrar"
        elif funcion.lower() == "d": #si es D voy a descifrar
            print(decifrar(texto, rotacion)) #invoco metodo "descifrar"
    else:
        print ("ERROR: Considere los argumentos: i|d 'cadena' rotacion(26 max)")

if __name__ == '__main__':
    main()