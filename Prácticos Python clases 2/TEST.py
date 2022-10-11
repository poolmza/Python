# def funcion_suma_sueldo ():
#     diccionario_sueldo_años = {
#         2019: 100000,
#         2020: 110000,
#         2021: 125000,
#         2022: 140000
#     }
#     suma_sueldo = 0
#     for sueldo in diccionario_sueldo_años.values():
#         suma_sueldo += sueldo
#     print ("SUMATORIA: ", suma_sueldo)
# funcion_suma_sueldo()

# ------------------------------------------------------------------------

# def funcion_suma_sueldo():
#     diccionario_sueldo_años = {
#         2019: 100000,
#         2020: 110000,
#         2021: 125000,
#         2022: 140000
#     }
#     suma_sueldo = 0
#     for sueldo in diccionario_sueldo_años.values():
#         suma_sueldo += sueldo
#     return suma_sueldo
# calculo_sumatoria = funcion_suma_sueldo()
# print ("Sumatoria de Sueldos devuelta por la Funcion: ", calculo_sumatoria)

# ------------------------------------------------------------------------

# def funcion_suma(parametro_a, parametro_b): #estos son los parametros
#     return (parametro_a+parametro_b)
# calculo_suma = funcion_suma(10 , 20) #estos son los argumentos
# print ("Sumatoria devuelta por la Funcion: ", calculo_suma) 

# ------------------------------------------------------------------------
# ---------------------Argumentos Posicionales----------------------------
# ------------------------------------------------------------------------

# def funcion_suma_sueldo(parametro_diccionario):
#     suma_sueldo = 0
#     for sueldo in parametro_diccionario.values():
#         suma_sueldo += sueldo
#     return suma_sueldo
# diccionario_sueldo_años = {
#     2019: 100000,
#     2020: 110000,
#     2021: 125000,
#     2022: 140000
# }
# calculo_sumatoria = funcion_suma_sueldo(diccionario_sueldo_años)
# print ("Sumatoria de Sueldos devuelta por la Funcion: ", calculo_sumatoria)

# ------------------------------------------------------------------------

# def funcion_suma_sueldo(parametro_diccionario):
#     suma_sueldo = 0
#     for sueldo in parametro_diccionario.values():
#         suma_sueldo += sueldo
#     return suma_sueldo
# diccionario_sueldo_años = {
#     2019: 100000,
#     2020: 110000,
#     2021: 125000,
#     2022: 140000
# }
# diccionario_sueldo_años_anteriores = {
#     2015: 55000,
#     2016: 60000,
#     2017: 75000,
#     2018: 80000
# }
# calculo_sumatoria = funcion_suma_sueldo(diccionario_sueldo_años)
# print ("Sumatoria de los ultimos Sueldos: ", calculo_sumatoria)
# calculo_sumatoria = funcion_suma_sueldo(diccionario_sueldo_años_anteriores)
# print ("Sumatoria de Sueldos Antiguos: ", calculo_sumatoria)

# ------------------------------------------------------------------------
# --------------------Argumentos Nominales--------------------------------
# ------------------------------------------------------------------------

# def funcion_suma(parametro_a, parametro_b):
#     return (parametro_a-parametro_b)
# calculo_suma = funcion_suma(parametro_b=10 , parametro_a=20)
# print ("Sumatoria devuelta por la Funcion: ", calculo_suma)

# Python permite mezclar el conceptos de parámetros nominales y posicionales 
# en una llamada a función, solo que los posicionales deben ir en primer lugar 
# antes (de izquierda a derecha) que los nominales.

# ------------------------------------------------------------------------
# --------------------Parámetros por defecto------------------------------
# ------------------------------------------------------------------------

# Es posible especificar valores por defecto en los parámetros de una función. 
# En el caso de que no se proporcione un valor al argumento en la llamada a la 
# función, el parámetro correspondiente tomará el valor definido por defecto.

# #EJ1 = 60
# def funcion_suma1(parametro_a=100, parametro_b=200, parametro_c=300):
#     return (parametro_a+parametro_b+parametro_c)
# calculo_suma = funcion_suma1(10, 20, 30)
# print ("Sumatoria devuelta por la Funcion: ", calculo_suma)

# # EJ2 = 330
# def funcion_suma2(parametro_a=100, parametro_b=200, parametro_c=300):
#     return (parametro_a+parametro_b+parametro_c)
# calculo_suma = funcion_suma2(10, 20)
# print ("Sumatoria devuelta por la Funcion: ", calculo_suma)

# # Ej3 = 240
# def funcion_suma3(parametro_a=100, parametro_b=200, parametro_c=300):
#     return (parametro_a+parametro_b+parametro_c)
# calculo_suma = funcion_suma3(10, parametro_c=30)
# print ("Sumatoria devuelta por la Funcion: ", calculo_suma)

# ------------------------------------------------------------------------
# ----------------Empaquetar/Desempaquetar argumentos---------------------
# ------------------------------------------------------------------------

# # EMPAQUETADO EN TOUPLA (*)

# def funcion_prueba(*parametro):
#     print ("Imprimo todos los elementos: ",parametro)
#     print ("Imprimo solo el primer elemento: ",parametro[0])
# funcion_prueba(10, 20, 30)

# def funcion_prueba(parametro_a, parametro_b, *parametros):
#     total = 0
#     for value in (parametro_a, parametro_b) + parametros:
#         total += value
#     return total
# valor_retornado = funcion_prueba(10, 20, 30, 40, 50)
# print ("Valor devuelto por la Funcion (1): " , valor_retornado)
# valor_retornado = funcion_prueba(10, 20)
# print ("Valor devuelto por la Funcion (2): " , valor_retornado)

# # EMPAQUETADO EN DICCIONARIO (**)

def funcion_prueba(**parametros):
    print("Diccionario completo: \n",parametros)
    print ("\n")
    for clave in parametros.keys():
        print (" Clave: ", clave, end=",")
        total = 0
    print ("\n")
    for value in parametros.values():
        print (" Valor: ", value, end=",") 
        total += value 
    print ("\n")
    return total

valor_retornado = funcion_prueba(a=10, b=20, c=30, d=40, e=50)
print ("Valor devuelto por la Funcion (1): " , valor_retornado,"\n")
valor_retornado = funcion_prueba(a=10, b=20)
print ("Valor devuelto por la Funcion (2): " , valor_retornado, "\n")

# # Modificando parámetros mutables
# pag 9

# def funcion_prueba(parametro_lista, parametro_atomico):
#     print("Lista dentro de la FC: ", parametro_lista)
#     print("Variable comun dentro de la FC: ", parametro_atomico)
#     parametro_lista[1] = 200
#     parametro_atomico = 2000
#     print("Variable comun dentro de la FC (modificado): ",
#     parametro_atomico)
# lista = [10,20,30,40,50]
# variable_comun = 1000;
# print("Lista antes de llamar a la FC: ", lista)
# print("Variable comun antes de llamar a la FC: ", variable_comun)
# funcion_prueba(lista,variable_comun )
# print("Lista despues de llamar a la FC: ", lista)
# print("Variable comun despues de llamar a la FC: ", variable_comun)

# 