# Escribir una función que reciba una frase y 
# devuelva un diccionario con las palabras que 
# contiene y su longitud.


frase = ("hola que tal como estas, estoy aqui para encontrarte.")

def fra_dic(frase):
    dicc_1 = {}
    listax = []
    for i in frase.split():
        dicc_1 [i] = len(i)
    
    listax.append(dicc_1)
    return listax

print(fra_dic (frase))