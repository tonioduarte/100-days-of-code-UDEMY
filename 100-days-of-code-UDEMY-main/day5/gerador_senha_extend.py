# .extend coloca a lista letra_aleatoria direto na lista senha, sem formar caixinhas dentro da senha
# .append adiciona mas forma as caixinhas

# com .extend = ['letra_aleatoria', 'numero_aleatorio', simbolo_aleatorio']
# com .append = [['letra_aleatoria'], ['numero_aleatorio'], ['simbolo_aleatorio']]

# o extend facilita na hora do for evitando de precisar entrar nas caixinhas
# for item in senha, direto, sem passar pelas caixinhas pq os itens ja estao em senha

# alem de senha se tornar a lista completa, conseguindo randomizar TODOS os itens dentro dela, sendo mais segura

import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nm_letras = int(input("Quantas letras você deseja? "))
nm_numeros = int(input("Quantos números você deseja? "))
nm_simbolos = int(input("Quantos símbolos você deseja? "))

senha = []

senha.extend(random.sample(letras, nm_letras))
senha.extend(random.sample(numeros, nm_numeros))
senha.extend(random.sample(simbolos, nm_simbolos))

random.shuffle(senha)   

senha_final = ""

for item in senha:
    senha_final += item

print("Senha gerada:", senha_final)
