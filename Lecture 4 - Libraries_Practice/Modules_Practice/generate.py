#---------------choice function ------------
# import random

# coin = random.choice(['h', 't'])
# print(coin)

#-----------to import only specific function-------
# from random import choice

# coin = choice(["Heads", "Tails"])
# print (coin)


#------------ randint function ---------------
# import random

# number = random.randint(1,10)
# print(number)

#-------------- shuffle function --------------
import random

cards = ["Jack", "King", "Queen"]
random.shuffle(cards)
# print(cards)
for card in cards:
    print(card)
