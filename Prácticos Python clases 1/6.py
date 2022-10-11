di1 = int(input("Dinero a invertir (hasta 5 años): "))
ia1 = int(input("Interes anual designado: "))
ia2 = (ia1/100+1)
na1 = int(input("Número de años a invertir: "))


ix1 = int(di1*ia2)
ix2 = int(ix1*ia2)
ix3 = int(ix2*ia2)
ix4 = int(ix3*ia2)
ix5 = int(ix4*ia2)
if (na1 == 1):
    print ("Capital obtenido año 1: ", ix1)
if (na1 == 2):
    print ("Capital obtenido año 1: ", ix1)
    print ("Capital obtenido año 2: ", ix2)
if (na1 == 3):
    print ("Capital obtenido año 1: ", ix1)
    print ("Capital obtenido año 2: ", ix2)
    print ("Capital obtenido año 3: ", ix3)
if (na1 == 4):
    print ("Capital obtenido año 1: ", ix1)
    print ("Capital obtenido año 2: ", ix2)
    print ("Capital obtenido año 3: ", ix3)
    print ("Capital obtenido año 4: ", ix4)
if (na1 == 5):
    print ("Capital obtenido año 1: ", ix1)
    print ("Capital obtenido año 2: ", ix2)
    print ("Capital obtenido año 3: ", ix3)
    print ("Capital obtenido año 4: ", ix4)
    print ("Capital obtenido año 5: ", ix5)
