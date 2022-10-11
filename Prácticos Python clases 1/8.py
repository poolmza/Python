# Solicitar al usuario que ingrese números, los cuales se guardarán en 
# una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
# Luego de que se termina la carga de la lista, solicitar al usuario 
# otro número y crear una lista con los elementos de la lista original 
# que sean menores que el número dado. Imprimir esta nueva lista, 
# iterando por ella.


#pag 23, 24, 25


print()
num=int(input("Ingrese un número o (cero) para finalizar: "))
lista=[]
while num!=0:
    lista.append(num)
    num=int(input("Ingrese un número o (cero) para finalizar: "))
print(lista)

num2=int(input("Ingrese un número para mostrar valores menores: \n"))
listafinal=[]
for elemento in lista:
    if elemento <= num2:
        listafinal.append(elemento)
print()
print("los números de menor valor son: \n", listafinal)
print()


