#zero-one knapsack. Es decir, sólo puedo tomar una cosa o no tomarla, pero no puedo tomar partes de ella

def morral(tamano_morral, pesos, valores, n):

    #Caso base
    if n==0 or tamano_morral==0: #Si ya no nos quedan elementos, o si ya no queda espacio en el morral
        return 0

    #Otro caso base
    if pesos[n-1]>tamano_morral: #Si el elemento que estoy analizando si meter o no al morral pesa más que lo disponible en el morral
        return morral(tamano_morral, pesos, valores, n-1)

    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1),
               morral(tamano_morral, pesos, valores, n-1))

if __name__ == "__main__":
    valores = [60, 100, 120] #$
    pesos = [10,20,30] #kg
    tamano_morral = 25 #kg
    n = len(valores) #en la primera llamada a morral, n vale 3

    resultado = morral(tamano_morral,pesos,valores,n)#cuál es el valor máximo que podemos obtener de las mezclas de estos valores
    print(resultado)