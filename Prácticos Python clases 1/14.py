# Cree un diccionario que contenga el nombre de una ciudad, 
# el país al que pertenece y la cantidad de habitantes que tiene. 
# Hacer un menú iterativo que permita al usuario realizar las siguientes 
# operaciones:
#      Agregar ciudades
#      Eliminar ciudades
#      Indicar la cantidad de habitantes en un país en particular
#      El porcentaje de habitantes en una ciudad de acuerdo al total registrado

# prov_arg = ("Buenos Aires","Catamarca","Chaco","Chubut","Córdoba","Corrientes","Entre Ríos","Formosa","Jujuy","La Pampa","La Rioja","Mendoza","Misiones","Neuquén","Río Negro","Salta","San Juan","San Luis","Santa Cruz","Santa Fe","Santiago del Estero","Tierra del Fuego","Tucumán","Antártida e Islas del Atlántico Sur")


dic_pais = {}
dic_ciu = {}

while True:
    print("\n")
    print("\033[0;34;47m" + "--------------Ingrese ciudades de Argentina--------------"+'\033[0;m')
    desicion=int(input("\n1_Ingresar una Ciudad \n2_Borrar una Ciuad\n3_Cantidad de habitantes de un Pais \n4_Porcentaje de habitantes de una ciudad \n\nSeleccione un numero: "))

    if desicion==1:
        ciudad=input("Ingrese Ciudad: ")
        pais=input("Ingrese el Pais al que pertenece: ")
        poblacion=int(input("Ingrese cantidad de población de la Ciudad: "))
        dic_ciu[ciudad] = poblacion
        dic_pais[pais] = dic_ciu
        
    if desicion==2:
        ciudad=input("Ingrese Ciudad a eliminar: ")
        del(dic_ciu[ciudad])
        
    if desicion==3:
        sum_ciu=sum(dic_ciu.values())
        print("\033[0;34m"+"Total de habitantes: ", sum_ciu,"."+'\033[0;m') 
    
    if desicion==4:
        sum_ciu=sum(dic_ciu.values())
        ciudad1=input("Ingrese Ciudad: ")
        porcentaje_ciu=dic_ciu[ciudad1] *100/sum_ciu
        print("\033[0;34m"+"\nEl porcentaje de habitantes de:", ciudad1, "es", round(porcentaje_ciu, 2), "%", "\ndel total de habitantes en el pais."+'\033[0;m')
        
    print()
    # print(dic_pais)
    print("\033[0;34m"+"Para el Pais",pais.upper(), "la cantidad de habitantes por ciudad es :\n", dic_pais[pais],"."+'\033[0;m')

















