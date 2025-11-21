import random 
import oi # importar uma biblioteca que esteja na MESMA pasta.

rad = random.randint(1, 100) #numero aleatorio
print(rad)
print(oi.C)
# dividir o codigo em modulos, para ficar mais facil saber oq está sendo feito, onde pessoas diferentes podem trablhar em modulos diferentes

rad01 = random.random() * 10 # agora vai até 10 (0 <= N < 10)
print(rad01) # vai printar numero aleatorios entre 0 e 1

radfloat = random.uniform(1, 5) # numero aleatorios em float
print(radfloat)

# print aleatorio, head or tail

hot = random.randint(1, 2)
if hot == 1:
    print(" Head ")
else:
    print(" Tail ")

# listas = estados_do_brasil = [ "Acre", "Amazonas" ...]
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

# Pedra, Papel e Tesoura
rps_robo = random.randint(1, 3)
rps_eu = input("rock, paper or scissors? ") # 1 = Rock, 2 = Paper, 3 = Scissor
if rps_eu == "rock" and rps_robo == 1:
    print(" The Robot choose Rock! Its a Tie! ")
elif rps_eu == "rock" and rps_robo == 2:
    print(" The Robot choose paper! The Robot Won! ")
elif rps_eu == "rock" and rps_robo == 3:
    print(" The Robot choose scissor! You Won! ")
if rps_eu == "paper" and rps_robo == 1:
    print(" The Robot choose Rock! You Won! ")
elif rps_eu == "paper" and rps_robo == 2:
    print(" The Robot choose paper! Its a Tie! ")
elif rps_eu == "paper" and rps_robo == 3:
    print(" The Robot choose scissor! The Robot Won! ")
if rps_eu == "scissors" and rps_robo == 1:
    print(" The Robot choose Rock! The Robot Won! ")
elif rps_eu == "scissors" and rps_robo == 2:
    print(" The Robot choose paper! You Won! ")
elif rps_eu == "scissors" and rps_robo == 3:
    print(" The Robot choose scissor! Its a Tie! ")
