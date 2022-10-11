# Dadas 2 listas A y B de igual número de elementos,
# se desea generar e imprimir una lista C conteniendo
# las sumas: A[i] + B[i] = C[i]. También indicar
# (solo imprimir por pantalla) aquellos elementos
# que están en A y no están en B.

A = ['Agua', 'Huevos', 'Aceite', 'chocolate', 'galletas']
B = ['Agua', 'Mandarinas', 'Café', 'chocolate', 'Talco']
C = [A+B]
# print(C)

D = []


def diferencias(lista_origen, lista_resta):
    for B in lista_resta:
        if B in lista_origen:
            lista_origen.remove(B)
    return lista_origen


print(diferencias(A, B))
