# Pedra, Papel e Tesoura
import random
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
