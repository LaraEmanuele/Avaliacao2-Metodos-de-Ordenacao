import math

def indiceFilhoEsquerda (indice):
    filhoEsquerda = (2*indice) +1
    return filhoEsquerda

def indiceFilhoDireita (indice):
    filhoDireita = (2*indice) + 2
    return filhoDireita

def indicePai (indice):
    pai = math.floor(((indice - 1)/2))
    return pai

def insertionHeap (lista, valor):
    lista.append(valor)
    i = len(lista) - 1
    p = indicePai (i)
    
    while lista[i] > lista[p]:
        lista[p], lista[i] = lista[i], lista[p]
        i = p
        p = indicePai (i)

def makeHeap (lista):
    listaHeap = []
    for i in range (len(lista)):
        insertionHeap (listaHeap, lista[i])
    
    return listaHeap

def HeapifyOrder (lista, tam, indice):
    maior = indice #indice pai - esperasse que seja maior que seus filhos
    esquerda = 2*indice +1 #indice do filho a esquerda
    direita = 2*indice +2#indice do filho a direita
    
    if esquerda < tam and lista[maior] < lista[esquerda]:
        maior = esquerda
    
    if direita < tam and lista[maior] < lista[direita]:
        maior = direita
        
    if maior != indice:
        lista[indice], lista[maior] = lista[maior], lista[indice]
        HeapifyOrder (lista, tam, maior)
        
        
def Heapify (lista, tam):
    if tam<=1:
        return
    ultimoIndice = tam - 1
    for i  in range ((int(ultimoIndice//2)), -1, -1):
        HeapifyOrder(lista, tam, i)
        
def removeHeap (lista):
    if len(lista) == 0:
        return lista
    
    removido = lista[0]
    lista[0] = lista[len(lista) -1]
    del (lista[len(lista) -1])
    
    HeapifyOrder(lista, len(lista), 0)
    
    return removido

def heapSort (lista):
    Heapify(lista, len(lista))
    for s in range (len(lista)-1, 0, -1): 
        lista[0], lista[s] = lista[s], lista[0]
        HeapifyOrder (lista, s, 0)
        
        
    
        

        
    
    
