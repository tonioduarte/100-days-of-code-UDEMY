# qual a nota mais alta?
notas_alunos = input(" quais são as notas?, separe-as por virgula ")
notamaior = 0
for notas in notas_alunos.split(","): #percorre cada valor digitado
    nota = float(notas) # converte a string para float
    if nota > notamaior: # se a nota atual for maior que a maior nota encontrada até agora
        notamaior = nota # atualiza notamaior com o novo valor

print("o maior número da lista é" , notamaior)