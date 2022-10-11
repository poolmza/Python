#  Cree un diccionario que contenga el nombre de una ciudad, el país al que
# pertenece y la cantidad de habitantes que tiene. Hacer un menú iterativo que
# permita al usuario realizar las siguientes operaciones:
# - Agregar ciudades
# - Eliminar ciudades
# - Indicar la cantidad de habitantes en un país en particular
# - El porcentaje de habitantes en una ciudad de acuerdo al total registrado


agenda = {}
while True:
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Cantidad de habitantes")
    print("5. Salir")
    
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        nombre = input("Nombre de la ciudad:")    
        if nombre in agenda:
            print("%s ya existe la ciudad su pais de origen es %s" % (nombre,agenda[nombre]))
            opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                numero = input("Agrega la nueva ciudad: ")
                agenda[nombre]=numero
        else:
            numero = input("Agrega el pais: ")
            agenda[nombre]=numero
            
    elif opcion == 2:
        cadena = input("Nombre de la ciudad a buscar:")    
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El nombre de la ciudad es %s del pais %s" % (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre de la ciudad a borrar:")    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe la ciudad")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre,"->",numero)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")

# -----------------------------------------------------------------------------------

# paises = {}


# def agregar_ciudad_pais(ciudad, pais):
#     global paises
#     if not pais in paises:
#         paises[pais] = []
#     paises[pais].append(ciudad)


# def imprimir_ciudades_de_pais(pais):
#     if not pais in paises:
#         print("No hay ciudades registrados")
#         return

#     print("Las ciudades de " + pais + " son: ")
#     for ciudad in paises[pais]:
#         print(ciudad)


# eleccion = ""
# while eleccion != "4":
#     eleccion = input("""
# 1. Agregar ciudad
# 2. Mostrar ciudades de pais
# 3. Eliminar ciudad
# 4. Salir
# Seleccione: """)
#     if eleccion == "1":
#         ciudad = input("Ingrese la ciudad: ")
#         pais = input("Ingrese el pais al que pertenece: ")
#         agregar_ciudad_pais(ciudad, pais)
#         print("Agregado")
#     elif eleccion == "2":
#         pais = input("Ingrese el pais: ")
#         imprimir_ciudades_de_pais(pais)

#     elif eleccion == "3":
#         ciudad = input("Ingrese la ciudad a borrar: ")
#         if ciudad in paises :
#             opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
#             if opcion == "s":
#                 del paises[ciudad]


