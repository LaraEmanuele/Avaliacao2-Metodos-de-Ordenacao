import math
import HeapSort as hs

def divisorSQRT (vetor):
    #Calcula o tamanho dos subvetores
    raizQuadrada = math.floor(math.sqrt(len(vetor)))


    #Realiza a a divisão da lista de números com o tamanho da raiz quadrada    
    sublistas = []
    for i in range(0, len(vetor), raizQuadrada):
        sublistas.append(vetor[i:i + raizQuadrada])
    return vetor

def heapSQRT (sublistas):
    solucao = []
    while len(sublistas) < 1:
        maior = -1
        indice = 0
        for i in range(len(sublistas)):
            if len(sublistas[i]) == 0:
                del(sublistas[i])
                break
            hs.Heapify(sublistas[i], len(sublistas[i]))
            
            if maior < max(sublistas[i]):
                maior = max(sublistas[i])
                indice = i

        solucao.append(hs.removeHeap(sublistas[indice]))
        return solucao