# Escriba una función en Python que indique si un número está en un determinado rango de numeros.
# Ej.:
# Entrada: valor=3; lim_inferior=2; lim_superior=5
# Salida: True

def num_rang(rango, numero):
    return numero in range(*rango)

lim_sup =int(input("Inicio de rango: "))
lim_inf =int(input("Final de rango: "))
lim_inf1 =int(lim_inf+1)
numero =int(input("Número a comprobar: "))

# print(num_rang)
print(num_rang ([lim_sup, lim_inf1], numero))
# print(num_rang)

if numero > lim_sup and numero < lim_inf1 :
    print("El número", numero, "está contenido en el rango de", lim_sup, "a", lim_inf)
else :
    print("El número", numero, "NO está contenido en el rango de", lim_sup, "a", lim_inf)
 
help('keywords')