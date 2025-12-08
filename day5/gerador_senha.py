import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nm_letras = int(input("Quantas letras você deseja? "))
nm_numeros = int(input("Quantos números você deseja? "))
nm_simbolos = int(input("Quantos símbolos você deseja? "))


senha = []

letra_aleatoria = random.sample(letras, nm_letras)
senha.append(letra_aleatoria)
numero_aleatorio = random.sample(numeros, nm_numeros)
senha.append(numero_aleatorio)
simbolo_aleatorio = random.sample(simbolos, nm_simbolos)
senha.append(simbolo_aleatorio)

random.shuffle(senha) # vai misturar as caixinhas

senha_final = "" # Cria a string pra deixar tudo junto
# Se printar só o senha vai sair tudo em lista

# senha = [['letra_aleatoria'], ['numero_aleatorio'], ['simbolo_aleatorio']]
# senha tem 3 caixinhas

for caixinha in senha: # vai ler uma caixinha de cada vez
    for item in caixinha: # vai entrar dentro de cada caixinha
        senha_final += item # vai unir todos os itens na string senha_final

print(f"sua senha pode ser {senha_final}")
# a randomização é incompleta nesse visto que nao mistura dentro das caixinhas, somente a ordem em q vai aparecer
# ou primeiro letra, ou primeiro numero e assim por diante





    




