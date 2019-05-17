# *- coding: utf-8 -*-
# DECLARANDO A CODIFICAÇÃO PARA ENTENDER ACENTOS 

"""  comentário
    de
    varias
    linhas """

print("-------\noperadores lógicos\n")
# OPERADORES LÓGICOS 

print(1 == 1 and 2 == 2)

print(1 == 2 or 1 == 1)

#######################################################
#if

print("\n-------\nIF\n")


if 1 == 1:
    print("1 = 1")

#######################################################
# else

print("\n-------\nELSE\n")

if 2 < 1: 
    print("nao vai aparecer")
else:
    print("isso tem q aparecer")

#######################################################
#elif

print("\n-------\nELIF\n")

if 2 == 1: 
    print("nao acontece nada")
elif 1 == 1:
    print("acontece isso")

#######################################################
#while

print("\n-------\nWHILE\n")

var = 1

while var <= 3:
    print(var)
    var += 1

#######################################################
#for

print("\n-------\nFOR\n")

lista = [3,2,1]

for i in lista:
    print(i)

#######################################################
#range()

print("\n-------\nRANGE\n")

#              de/até/de quanto em quanto     
for i in range(10,20,2):
    print(i)

#######################################################
#input()

print("\n-------\nINPUT\n")

numero = input("informe um numero: ")

print("o numero difitado é " + numero)

#######################################################
#FUNCOES DE STRING

print("\n-------\nFUNCOES DE STRING\n")

print ("tamanho da string => len(string)")
print ("navegando pelo indice => string[n]")
print ("pegar de n a m  => string[n:m]")

#######################################################
#CRIAR FUNCOES 

print("\n-------\nFUNCOES\n")

def printVerdade():
    return "rafael lindao"

print(printVerdade())

#######################################################
#MODOS DE LEITURA 

""" 
    r   =>  somente leitura
    w   =>  escrita(irá substituir caso ja tenha algo escrito)
    a   =>  leitura e escrita (adiciona algo no fim do texto ja escrito)
    r+  =>  leitura e escrita
    w+  =>  escrita (tambem substitui o conteudo)
    a+  =>  leitura e escrita (abre o arquivo para atualizaçao)
"""
# var = open(nomedoArquivo, modeDeLeitura)
# read()        =>  le o arquivo inteiro
# readlines()   =>  coloca todas linhas em uma lista
# arquivo.write("escrever no arquivo")
# arquivo.close()  => nao obrigatório mas recomendado 


"""
try:
    caso isso retorne erro
except:
    faz isso
"""
"""
    if a not in b       se nao esta 
"""