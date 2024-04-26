import CRArquivos as cra
import HeapSort as hs
import InsertionSort as inso
import math
import time

lista = [4,2,8,7,1,5,3,6,10]

raizQuadrada = math.floor(math.sqrt(len(lista)))
    
sublistas = []
for i in range(0, len(lista), raizQuadrada):
    sublistas.append(lista[i:i + raizQuadrada])
print("A sublistas V são: ", sublistas)

#inicio = time.time()

solucao = []
ultimosElementos = []
for i in sublistas:
    hs.heapSort(sublistas[i])
    print("As sublistas depois do heap sao: ", sublistas)
    maxValue, maxIndex = max(enumerate(sublistas), key=lambda item: item[1])
    solucao.append(maxValue)
    del(sublistas.maxIndex[-1])
        
print("A solucao do sqrt: ", solucao)
    
    
    
#fim = time.time()
#duracao = fim - inicio