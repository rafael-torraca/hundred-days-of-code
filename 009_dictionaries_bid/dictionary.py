nato_phonetic_alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta"
}

print(nato_phonetic_alphabet["A"])
print(nato_phonetic_alphabet["B"])
# print(nato_phonetic_alphabet["E"])

for key in nato_phonetic_alphabet:
    print(key)

for key, value in nato_phonetic_alphabet.items():
    print(f"{key}: {value}")

nato_phonetic_alphabet["B"] = "Brabaoooo"

for key in nato_phonetic_alphabet.keys():
    print(key)

for value in nato_phonetic_alphabet.values():
    print(value)
