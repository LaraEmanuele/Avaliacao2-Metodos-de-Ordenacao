import CRArquivos as cra

def InsetionSort (lista):
    #O n é tamanho do vetor
    n = len(lista)
    
    for i in range (1,n):
        chave = lista[i]#Elemento desordenado
        j = i-1# Elemento da sublista ordenada
        while j >=0 and lista[j]>chave:
            lista[j+1] = lista [j]
            j = j - 1
        lista [j+1] = chave
    return lista [len(lista) - 1]