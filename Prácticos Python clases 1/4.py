#Leer una secuencia de números y determinar 
# el mayor de los pares leídos.



numero = int(input("ingrese un numero: "))
mayor = 0
while numero > 0 :
    if numero % 2 == 0:
        if numero > mayor:
            mayor = numero
    numero = int(input("Ingrese un numero:"))
print("El mayor de todos es: ", mayor)

