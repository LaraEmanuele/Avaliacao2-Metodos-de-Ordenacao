import CRArquivos as cra
import SqrtSort as sq
import InsertionSort as inso
import HeapSort as hs
import math
import time
import itertools

vetor = [4,2,8,7,1,5,3,6,10]

subvetor = sq.divisorSQRT(vetor)

for i in range (len(subvetor)):
    hs.Heapify(subvetor[i], len(subvetor))

solucao = []
aux = []
count = 0

while len(aux) != 0:
    for i in range (len(subvetor)):
        hs.insertionHeap(aux,hs.removeHeap(subvetor[i]))

    solucao.append(hs.removeHeap(aux[i]))
    
print("A solucao e: ", solucao)