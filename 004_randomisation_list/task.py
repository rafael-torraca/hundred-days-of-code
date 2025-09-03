from random import choice, randint


friends = ["Rafael", "Fernanda", "Gabriel", "Marilia", "Joao Batista"]

random_choice = choice(friends)
print(random_choice)


list_size = len(friends)
random_range = randint(0, list_size-1)
print(friends[random_range])
