# Dado una lista de 10 nombres de personas, realice un programa que
# cargue la lista, la ordene de forma ascendente y la muestre por
# pantalla ordenado. Python nos brinda la función “sorted” para
# realizar dicho procedimiento, pero la idea es que el ejercicio
# se resuelva utilizando algoritmia propia de algún método de
# ordenamiento existente.

def ord_abc (arreglo):
    n=len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1]=arreglo[j+1],arreglo[j]

nom = ['Carlos', 'Juan', 'Miguel', 'Pablo', 'Saul', 'Ricardo', 'Silvio', 'Diego', 'Andrés', 'Vanesa']
ord_abc(nom)
print(nom)
