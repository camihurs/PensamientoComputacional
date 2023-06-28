def divide_elementos_de_lista(lista,divisor):
    #Programación defensiva
    try:
        return [i / divisor for i in lista]

    except ZeroDivisionError as e: #Manejamos la excepción, y el programa no falla, no muestra error,solo devuelve la lista
        print(e) #Imprimimos el tipo de error. Es opcional.
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista,divisor))