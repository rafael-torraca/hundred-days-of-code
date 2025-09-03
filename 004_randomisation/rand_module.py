import random
from my_module import my_favourite_number

random_integer = random.randint(1, 3)

print(random_integer)
print(my_favourite_number)
print(type(random_integer))

random_number_0_to_1 = random.random()

print(random_number_0_to_1)
print(type(random_number_0_to_1))

random_float = random.uniform(0, 10)

print(random_float)
print(type(random_float))
