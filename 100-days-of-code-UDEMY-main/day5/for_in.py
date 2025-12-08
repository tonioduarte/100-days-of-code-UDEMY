# loops, uso do for
frutas = {"Uva", "Melão", "Maçã"}
for fruta in frutas:
    print(fruta)
    print("mousse de " + fruta) # ("mousse de %s" % fruta)

notasescola = {10, 9, 4, 8, 3, 8, 5, 7}
notas_totais = sum(notasescola) # soma todas os nums da lista
print(notas_totais)
# ou fazer assim:

# sum = 0
# for notas in notasescola
#   sum += score
# print(sun)

print(max(notasescola)) # pega o maior numero da lista