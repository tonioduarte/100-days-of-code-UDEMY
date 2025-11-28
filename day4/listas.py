# listas = estados_do_brasil = [ "Acre", "Amazonas" ...]
import random
lista_compras = ["Arroz","Feijão","Doces","Leite"] # arroz = 0, feijão = 1....
lista_compras[1] = "Detergente" # troca o item desejado
lista_compras.append("Mousse") # adiciona + 1 item, .extend cria uma nova lista e adiciona ela com a primeira, .extend( = [""])
print(lista_compras)

friends = ["Antônio", "Julia", "Bárbara", "Letícia"]
random_friends = random.choice(friends) # random.choice escolhe coisas dentro de listas aleatoriamente, faz a lista primeira coloca no random choices e printa ele
print(random_friends)

compras_amigos = [lista_compras, friends]
print(compras_amigos [0][1]) # o primeiro 0 refere-se a lista 1, já o 1 reference ao item na lista 1, se fosse [1][0] ia printar o primeiro item da lista 2.
# não esquecer q as coisas contam a partir do 0!
