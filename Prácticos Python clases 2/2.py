# Escriba una función en Python que indique si un número es perfecto. 
# Utilice una función auxiliar que calcule los divisores propios.
# Nota: Un número perfecto es un número entero positivo que es igual 
# a la suma de sus divisores positivos.
# Ej.:
# Entrada: 6 (1+2+3)
# Salida: True


def perfecto(parametro_numero):
    suma=0
    for i in range(1,parametro_numero,1):
        if parametro_numero%i==0:
            suma=suma+i
            # ptint("es divisor", i)
    if suma == parametro_numero:
        return 1
    else:
        return 0

numero =int(input("ingrese numero: "))
resultado=perfecto(numero)
if resultado==1:
    print("el numero ingresado:", numero, "SI es perfecto")
else:
    print("el numero ingresado", numero, "NO es perfecto")

        
