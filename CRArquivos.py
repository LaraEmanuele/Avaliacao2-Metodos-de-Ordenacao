import os
import random

"""
Esse modulo gera um arquivo contendo uma lista de inteiros aleatórios desordenados de tamanho n e realiza sua leitura
"""

def gerarListaDesordenada(n):
    diretorio_atual = os.getcwd()
    numeros = set()
    count = 0
    with open(os.path.join(diretorio_atual, "Dados",
                   f"ListaDesordenada_{n}.txt"), "w") as arquivo:
        while count < n:
            numeroAleatorio = random.randint(0, (10*n))
            if numeroAleatorio not in numeros:
                arquivo.write(str(numeroAleatorio) + "\n")
                numeros.add(numeroAleatorio)
                count += 1


def leArquivoTimeInsertion(n):
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "Dados",
                   f"DadosTimeInstion_{n}.txt"), "r")
    numeros = []

    for linha in arquivo:
        numero = linha.strip()
        numeros.append(float(numero))

    arquivo.close()
    return numeros

def leArquivoTimeHeap(n):
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "Dados",
                   f"DadosTimeHeap_{n}.txt"), "r")
    numeros = []

    for linha in arquivo:
        numero = linha.strip()
        numeros.append(float(numero))

    arquivo.close()
    return numeros
