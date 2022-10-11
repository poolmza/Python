# Los empleados de una fábrica trabajan en dos turnos, 
# Diurno y Nocturno. Se desea calcular el jornal diario 
# de acuerdo a las siguientes reglas:
#  La tarifa de las horas diurnas es de $350
#  La tarifa de las horas nocturnas es de $400
#  En caso de ser festivo, la tarifa se incrementa en 
# un 10% en caso de turno diurno y en un 15% para el nocturno.
# 
# Desarrolle una función que permita ingresar por teclado 
# la siguiente información para, al menos, 2 empleados, 
# nombre del trabajador, 
# el número de horas trabajadas, 
# el turno y 
# el tipo de día (“Festivo”, “Laborable”), 

# para ello se podría utilizar 1 “diccionario” para registrar 
# la información y si los datos ingresados son correctos 
# llamar a otra función que realice el cálculo del sueldo 
# a cobrar en ese día. 
# Mostrar por pantalla los datos 
# ingresados y el sueldo calculado 
# para cada empleado.


while True:
    nombre=str(input("\nIngrese nombre del empleado: "))
    while True:
     try:
         horas = int(input("Ingrese horas trabajadas: "))
         break
     except ValueError:
         print("Debes escribir un numero!")

    turno = int(input("Ingresar tipo de turno:\n1)Diurno\n2)Nocturno\nSeleccione una opcion: "))
    while turno not in(1,2):
        turno = int(input("\nIngresar tipo de turno:\n1)Diurno\n2)Nocturno\nSeleccione una opcion: "))
        
    tipo_d_dia = int(input("\nIngresar tipo de día:\n3)Laborable\n4)Festivo\nSeleccione una opción: "))
    while tipo_d_dia not in (3,4):
        tipo_d_dia = input("Ingresar tipo de día:\n3)Laborable\n4)Festivo\nSeleccione una opción: ")
    
    lista_tres= []
    
    def empleado(nombre, horas, turno, tipo_d_dia): #se encuentra dentro del while
        empleados = {}
        empleados[nombre]= [horas, turno, tipo_d_dia]
        lista_tres.append(empleados)
        return lista_tres

    def calculo(lista_tres):
        for i in lista_tres:
            trabajador = list(i.keys())
            datos = list(i.values())
            for i in range(len(datos)):
                if 1 in datos[i]:
                    if 3 in datos[i]:
                        print(f"{trabajador[0]} debe cobrar la cantidad de: {datos[i][0]*350}")
                    else:
                        print(f"{trabajador[0]} debe cobrar la cantidad de: {datos[i][0]*1.1*350}")
                else:
                    if 3 in datos[i]:
                        print(f"{trabajador[0]} debe cobrar la cantidad de: {datos[i][0]*400}")
                    else:
                        print(f"{trabajador[0]} debe cobrar la cantidad de: {datos[i][0]*1.15*400}")

            
    
    empleado(nombre, horas, turno, tipo_d_dia)
    calculo(lista_tres)



