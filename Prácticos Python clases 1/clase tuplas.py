#pagina 31

# diccionario_sueldo_años = {}
# sueldo_inicial = 95000
# for i in range(2018, 2022):
#     sueldo_inicial += 5000
#     diccionario_sueldo_años[i] = sueldo_inicial
# print(diccionario_sueldo_años)

########

# diccionario_sueldo_años = {}
# sueldo_inicial = 95000
# for i in range(2018, 2022):
#     sueldo_inicial += 5000
#     diccionario_sueldo_años[i] = sueldo_inicial
# for clave in diccionario_sueldo_años: #para imprimir las claves tb podriamos usar .keys()
#     print(clave)
# for sueldo in diccionario_sueldo_años.values():
#     print(sueldo)

##########

diccionario_sueldo_años = {}
sueldo_inicial = 95000
for i in range(2018, 2022):
    sueldo_inicial += 5000
    diccionario_sueldo_años[i] = sueldo_inicial
for clave, sueldo in diccionario_sueldo_años.items():
    print("Para la clave: ",clave, " corresponde el valor: ", sueldo)

###########

