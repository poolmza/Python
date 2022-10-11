# Escriba una función en Python que reciba como parámetro una frase y 
# 1 carácter, y devuelva si ese carácter se encuentra dentro de la frase. 
# Además de ello, la función debe poder indicar la cantidad de palabras 
# que hay en la frase.
frace = input("Ingresar frace: ")
caracter = input("Ingresar caracter: ")

def caracter_in_frace (frace, caracter):
    fragmentado=frace.split()
    if caracter in frace:
        print (f" \nEl caracter {caracter} se encuentra \n dentro de la frace")
    else :
        print(f" \nEl caracter {caracter} No se encuentra \n dentro de la frace")
    print (f" y la frace tiene {len(fragmentado)} palabras\n")
    # print ("\n","La cantidad de palabras\n", "en la frace es de: ", len(frace.split()),".", "\n")

caracter_in_frace(frace, caracter)

