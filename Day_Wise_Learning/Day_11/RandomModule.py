import random
# print(round(random.random(),2))
# print(random.uniform(1000,100000000))
# print(random.randint(10,20))
# print(random.randrange(10,50,2))



#Sequence Related functions
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

random.shuffle(cards)

print(random.choice(cards))
print(random.choice(cards)) #Without replacement
print(random.sample(cards,k=3)) #With replacement

random.seed(456)
print(random.random())

