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
entrada = input("Escribe una palabra: ")

    

# Proceso

if ord(entrada [0]) == ord("A"):
    resultado = str(entrada[0]) + " comineza con 'A'"

elif ord(entrada [0]) == ord("Á"):
    resultado = str(entrada[0]) + " comineza con 'A'"

elif ord(entrada [0]) == ord("a"):
    resultado = str(entrada[0]) + " comineza con 'A'"

elif ord(entrada [0]) == ord("á"):
    resultado = str(entrada[0]) + " comineza con 'A'"

else:
    resultado = str(entrada[0]) + " no comienza con 'A' "

# Salidas
print(resultado)
