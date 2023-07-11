import numpy as np
import math
import matplotlib.pyplot as plt

def read_book(url):
   # Leemos el libro con una url y regresamos el contenido
   file = open(url,"r",encoding='UTF-8')
   content = list()
   if file.mode == 'r':
       content = file.read()
   return content


# Contará cuántas veces aparece cada símbolo a lo largo del libro.
def probability_per_symbol(book,alphabet):

   # Tamaño de nuestro alfabeto
   size = len(alphabet)

   # Tamaño del libro (total de caracteres)
   bookSize = len(book)

   # Vector donde guardaremos la probabilidad de cada símbolo
   Probability = np.zeros(size)

   for i in range(size):
       reps = 0
       # Símbolo actual en que contará las repeticiones
       current_symbol = alphabet[i]
       for j in range(bookSize):
           # Símbolo con el que lo comparará
           symbol = book[j]

           #Si son iguales entonces ha aparecido y se suma el contador
           if symbol == current_symbol:
               reps+=1

       # Asigna la probabilidad de aparición del símbolo en turno
       Probability[i] = reps/bookSize

   return Probability


#Para terminar necesitamos calcular la información de cada símbolo.
def information_per_symbol(Probability, size_alphabet):

 # Vector vacío de información por símbolo
 Information = np.zeros(size_alphabet)

 #Recorremos todo el alfabeto
 for i in range(size_alphabet):
     p_by_symbol = Probability[i]
     # Se calcula la información de cada símbolo
     if p_by_symbol != 0:
         Information[i] = math.log2(1/p_by_symbol)
     else:
         Information[i] = 0

 return Information


def calc_entropy(Probability, Information):
   # Vector de entropía vacío
   h = np.zeros(len(Probability))

   # Cálculo de entropía que es la probabilidad del símbolo por la información de cada símbolo
   for i in range(len(Probability)):
       h[i]=Probability[i]*Information[i]

   # Se realiza la suma para acumular el cálculo de la entropía
   H = sum(h)

   return H


def plot_bar_Probabilities(alphabet,probabilities):
     # this is for plotting purpose
     index = np.arange(len(alphabet))
     plt.figure(1)
     plt.bar(index, probabilities)
     plt.xlabel('Símbolo', fontsize=12)
     plt.ylabel('Probabilidad', fontsize=12)
     plt.xticks(index, alphabet, fontsize=10)
     plt.title('Probabilidades por cada símbolo del alfabeto')


def plot_bar_Information(alphabet,Information):
     # this is for plotting purpose
     plt.figure(2)
     index = np.arange(len(alphabet))
     plt.bar(index, Information)
     plt.xlabel('Símbolo', fontsize=12)
     plt.ylabel('Información', fontsize=12)
     plt.xticks(index, alphabet, fontsize=10)
     plt.title('Información por símbolo')


if __name__ == "__main__":
    #Para calcular la información dada por cada símbolo primero necesitamos definir nuestro alfabeto, esto es sencillo,
    # solo colocaremos una lista que contenga cada símbolo del abecedario en español contemplando el espacio como un símbolo.

    ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    # Tamaño del alfabeto
    size_alphabet = len(ABC)

    #Leemos el libro
    book = read_book('el_principito.txt')

    # Tamaño del libro
    bookSize = len(book)

    #Calculamos la probabilidad de cada símbolo de nuestro alfabeto
    P = probability_per_symbol(book, ABC)
    print("Probabilidades: ", P)

    #Calculamos la información otorgada por cada símbolo
    I = information_per_symbol(P, size_alphabet)
    #Con esta relación se puede ver que mientras más probable sea que aparezca un símbolo menos información nos otorgará y
    # viceversa. Usando el ejemplo del libro que analizaremos, las palabras como los artículos “el”, “la” o “una” no otorgan mucha
    # información debido a que aparecen constantemente, es decir, su probabilidad de aparición es alta por lo que no nos dan mucho
    # significado y aportan poca información. Al contrario de los nombres propios como “México” que otorgan mucha información, ya
    # que su aparición es menos frecuente. Esto es obviamente condicionado a nuestra fuente de información S.

    print("Información de cada símbolo: ", I)

    #Con los valores de: 1) la probabilidad de aparición de cada símbolo y 2)la información de cada uno podemos calcular la entropía de
    #nuestra fuente de información

    # La entropía es la información promedio que nos otorga una fuente, en este caso es cuántos bits se necesitan en promedio por símbolo
    # para representar la información de nuestra fuente. El cálculo de la entropía está dado por:

    #La entropía es la suma ponderada de la información de cada símbolo. Esta está ponderada por la probabilidad de aparición de dicho
    # símbolo, su unidad de medida es en bits.

    Entropia = calc_entropy(P,I)
    print("Entropia: ", Entropia)

    plot_bar_Probabilities(ABC,P)
    plot_bar_Information(ABC,I)
    plt.show()

    # Análisis de entropía del libro
    print(f"La información promedio de cada símbolo es de (Entropía): {Entropia} bits")
    print(f"La longitud del libro es: {bookSize} símbolos")
    print(f"La información promedio contenida por esta fuente de información es {bookSize*Entropia / 8000} kB")