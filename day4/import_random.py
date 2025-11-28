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