# Escriba una función en Python que reciba una lista de valores 
# enteros y devuelva otra lista sólo con aquellos valores pares.
# Ej.:
# Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Salida: [2, 4, 6, 8]

valores = []
for num in range(0,200):
    valores.append(num)

def filtro_pares(valores):
    filtrado = []
    for i in range(1,len(valores)+1):
        if i % 2 == 0:
            filtrado.append(i)
    
    return filtrado

print(filtro_pares(valores))