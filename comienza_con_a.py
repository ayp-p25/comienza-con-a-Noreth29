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
if int(entrada)  >= 1 and int(entrada) <= 9:
    resultado = "Error. Escribe una palabra"

else:
    if ord(entrada [0]) == ord("A"):
        resultado = entrada + " comineza con 'A'"

    elif ord(entrada [0]) == ord("Á"):
        resultado = entrada + " comineza con 'A'"

    elif ord(entrada [0]) == ord("a"):
        resultado = entrada + " comineza con 'A'"

    elif ord(entrada [0]) == ord("á"):
        resultado = entrada + " comineza con 'A'"

    else:
        resultado = entrada + " no comienza con 'A' "

# Salidas
print(resultado)
