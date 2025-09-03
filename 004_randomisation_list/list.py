states_of_brazil = [
    "São Paulo",
    "Minas Gerais",
    "Rio de Janeiro",
    "Santa Catarina",
    "Rio Grande do Sul",
    "Mato Grosso",
    "Mato Grosso do Sul",
]


print(states_of_brazil[0])
states_of_brazil[0] = "Acre"
print(states_of_brazil[0])
print(states_of_brazil[2])
print(states_of_brazil[-1])
states_of_brazil.append("Tocantins")
print(states_of_brazil[-1])

states_of_brazil.extend(["RafaelLand", "Hacking"])

print(states_of_brazil)
