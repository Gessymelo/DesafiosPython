##  Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

#definindo vetores

idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {} (em metros): ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

print("\nIdades e alturas em ordem inversa:")

for i in range(4, -1, -1):
    print("Pessoa {}: Idade = {}, Altura = {}m".format(i+1, idades[i], alturas[i]))