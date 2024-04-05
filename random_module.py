import random

#a = random.randint(1, 3)
#a = random.randrange(1, 7)
#a = random.random()
#a = random.uniform(1, 3)

b = [3, 4, 6, 8, 0, 15, 19, -3, 7, 4, -69]
#random_elements = random.choice(b)
random.shuffle(b)

print(b)