#Crescimento da população Brasileira 1980-2016
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

#plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle="-")
plt.title("CRESCIMENTO DA POPULAÇÃO BRASILEIRA")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()

#plt.savefig("populacaobrasileira.png", dpi="3000")