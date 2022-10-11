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

# -------------------------------------------------------------------
# -------------------------------------------------------------------

# abc= list('abcdefghijklmnñopqrstuvwxyz')
# nom.sort(key=lambda p: p.lower().replace("á", "a").\
#     replace("é", "e").replace("í", "i")\
#     .replace("ó", "o").replace("ú", "u"))

# print()
# print("La lista sin Sorted es: \n", nom)
# print("La lista con Sorted es: \n",sorted(nom))
# print()

# nom.sort(key=lambda p: p.lower().replace("á", "a").\
#         replace("é", "e").replace("í", "i")\
#         .replace("ó", "o").replace("ú", "u"))
# print (nom)



# -------------------------------------------------------------------
# def ord_abc (arreglo):
#     longitud = len(arreglo)
#     for i in range(longitud-1):
#         print('rango del longitud (i): ' + str(i))
#         for j in range(longitud-1-i):
#             print('rango de longitud - 1 - i (j): ' + str(j))
#             print(arreglo[j])
#             if arreglo[j] > arreglo[j+1]:
#                 arreglo[j], arreglo[j+1]=arreglo[j+1],arreglo[j]

# nom = ['Carlos', 'Juan', 'Miguel', 'Pablo', 'Saul', 'Ricardo', 'Silvio', 'Diego', 'Andrés', 'Vanesa']
# ord_abc(nom)
# print(nom)
# -------------------------------------------------------------------

# datos = ['Carlos', 'Juan', 'Miguel', 'Pablo', 'Saul', 'Ricardo', 'Silvio', 'Diego', 'Andrés', 'Vanesa']
# auxiliar=''
# for i in range(len(datos)):
#     for j in range (i+1, len(datos)):
#         print("comparo: ", datos[i], " con", datos[j])
#         if(datos[i].lower()>datos[j].lower()):
#                 auxiliar = datos[i]
#                 datos[i] = datos[j]
#                 datos[j] = auxiliar
#                 print(datos)

# -------------------------------------------------------------------

# nombres = ['Carlos', 'Juan', 'Miguel', 'Pablo', 'Saul',
#        'Ricardo', 'Silvio', 'Diego', 'Andrés', 'Vanesa']

# abc = list('abcdefghijklmnñopqrstuvwxyz')

# nombres_ordenados = {}

# for nombre in nombres:
#     for letra in abc:
#         if str(nombre[0]).lower() == str(letra):
#             print('coincide')
#             print(abc.index(letra))
#             nombres_ordenados.append()
            # nombres_ordenados.nombre = nombre
            # nombres_ordenados.posicion = abc.index(letra)
            # print(nombres_ordenados)

    

# -------------------------------------------------------------------

# CantElementos = len(nom)
# for lazo1 in range(CantElementos-1):

#     for lazo2 in range(CantElementos-1-lazo1):

#         if nom[lazo2].lower() > nom[lazo2+1].lower():

#             temporal = nom[lazo2]
#             nom[lazo2] = nom[lazo2+1]
#             nom[lazo2+1] = temporal

#         print(nom)
#     print("----")

# -------------------------------------------------------------------

# nombres = ['Walter', 'Diego', 'julia', 'Luis', 'Marcela', 'Cristina']
# CantElementos = len(nombres)

# for lazo1 in range(CantElementos-1):

#     for lazo2 in range(CantElementos-1-lazo1):

#         if nombres[lazo2].lower() > nombres[lazo2+1].lower():

#             temporal = nombres[lazo2]
#             nombres[lazo2] = nombres[lazo2+1]
#             nombres[lazo2+1] = temporal

#         print(nombres)
#     print("----")

# -------------------------------------------------------------------


# ESTA FUNCIONA
# def my_sort(lista):
#     largo = len(lista)
#     if largo == 0:
#         return
#     idx = 0
#     min = lista[idx]
#     min_prev = None
#     found = True
#     while found:
#         for index in range(largo):
#             if lista[index] < min and (min_prev == None or lista[index] > min_prev):
#                 idx = index
#                 min = lista[idx]
#                 found = True
#         if found:
#             yield min
#             for index in range(idx + 1, largo):
#                 if lista[index] == min:
#                     yield min
#             found = False
#             for index in range(largo):
#                 if lista[index] > min:
#                     idx = index
#                     found = True
#                     break;
#             min_prev = min
#             min = lista[idx]

# for test in nom:
#     print()
#     print("Lista original:\n", test)
#     print("Lista ordenada:\n", [value for value in my_sort(test)])
#     print()
