lista = [] # [] = lista

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        lista.append("FizzBuzz")
    elif number % 5 == 0:
        lista.append("Buzz")
    elif number % 3 == 0:
        lista.append("Fizz")
    else:
        lista.append(number)

print(lista)