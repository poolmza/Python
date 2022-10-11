# Cree un diccionario con los nombres de 5 personas de su familia 
# y sus edades. 
# Indicar el integrante más grande y el mas chico.

# --------------values-----------------------------------
# trae los valores que se encuentran en el diccionario a 
# la derecha de los ":"

# ---------------keys------------------------------------
# trae los valores que se encuentran en el diccionario a 
# la izquierda de los ":"



nombres = {
    'Daniel':'67', 
    'Elizabeth':'39', 
    'Mariano':'41', 
    'Romina':'37' , 
    'Margarita':'69'
    }

edad_minima = min(nombres.keys(), key=lambda k: nombres[k])
edad_maxima = max(nombres.keys(), key=lambda j: nombres[j])
print()
print("El integrante de la familia mas longevo es", edad_maxima, "con", nombres[edad_maxima], "años.")
print()
print("El integrante de la familia mas joven es", edad_minima,"con", nombres[edad_minima], "años.")
print()


