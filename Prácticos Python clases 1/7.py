cm = int(input("Cuota mensual sin iva: "))
cm30 = (cm*0.3)
cm030 = (cm - cm30)
icm = int(cm*0.21)
icm_10 = int(icm*0.1)   #10% del iva
icm010 = (icm-icm_10) #iva - 10%
print ("El iva correspondiente es: $", icm)
print ("Total: $", cm+icm_10)

mat1 = int(input("Materia 1: "))
mat2 = int(input("Materia 2: "))
mat3 = int(input("Materia 3: "))
mat4 = int(input("Materia 4: "))
mat5 = int(input("Materia 5: "))
mat6 = int(input("Materia 6: "))
prom = ((mat1+mat2+mat3+mat4+mat5+mat6)/6)
print ("promedio: ", prom)

if (prom >= 4):
    print ("Corresponde pagar de matrícula: $",cm030) 
    print ("Corresponde pagar de iva: $0") 
    print ("Total a pagar: $", cm030)
if (prom < 4):
    print ("Corresponde pagar de matrícula: $",cm) 
    print ("Corresponde pagar de iva: $", icm010) 
    print ("Total a pagar: $", cm+icm010)