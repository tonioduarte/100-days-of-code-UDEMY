#int = numero inteiro
#float = numero quebrado
#round = arrendondar

# PEMDAS

#()
#** = Exponencial
#* = Multiplicação
#/ = Divisão
#// = Divisão sem resto 
#+
#-
height = 1.65
weight = 84 
#bmi = weight // height **2
bmi = weight / height **2
print (int(bmi))


score = 0
# o user faz um ponto
score += 1 
print(score)

#f string = concatenar dados diferentes em uma string

beauty = 10
prettiness = 100.0
beautiful = True

print(f" Your beauty is {beauty}, your prettiness is {prettiness}, are u beautiful? {beautiful}")

#bill calculator
print(' Welcome to the bill calculator')
bill = float(input(' What was the total bill? '))
print (bill)
tip = int(input(' how much tip would u give? 10,12 or 0 '))
print(tip)
people = float(input(" how many people to split? "))
if tip == 10: 
    total = bill * 1.10
elif tip == 12:
    total = bill * 1.12
elif tip == 0:
    total = bill * 1
else:
    total = bill
    print(" tip not recognize")

split = round(total / people)
print (" each person should pay " + str(split))