"""
Comienza con A
"""

# Declaraciones
#Pedir entrada
#Si comienza con A
#Si comienza con a
#Si comienza con Á
#Si comienza con á

# Entradas
palabra = input("Escribe una palabra: ")
entrada = str(palabra[0])
    

# Proceso

if ord(entrada) == ord("A"):
    resultado = "'" + palabra + "'" + " comienza con 'A'"

elif ord(entrada) == ord("Á"):
    resultado = "'" + palabra + "'" + " comienza con 'A'"

elif ord(entrada) == ord("a"):
    resultado = "'" + palabra + "'" + " comienza con 'A'"

elif ord(entrada) == ord("á"):
    resultado = "'" + palabra + "'" + " comienza con 'A'"

else:
    resultado = "'" + palabra + "'" + " no comienza con 'A' "

# Salidas
print(resultado)
