# Leer una secuencia de 10 números, almacenarlos en
# una lista y mostrar la suma de los elementos que
# ocupan posiciones pares y el mayor número de los
# que ocupan posiciones impares.


num = []
num2 = []

for i in range(11):
    if i % 2 == 0:
        num.append(i)

    else:
        i % 3 == 0
        num2.append(i)

print("Los números pares son: \n", num)
print("La suma de los valores pares da: ", sum(num))
print()
print("Los números impares son: \n", num2)
print("La suma de los valores impares da: ", sum(num2))
print("El mayor de los impares es: ", max(num2))
print()
