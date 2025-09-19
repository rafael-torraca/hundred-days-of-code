def calculate_love_score(name1, name2):
    true_list = ["T", "R", "U", "E"]
    love_list = ["L", "O", "V", "E"]
    name1 = name1.upper()
    name2 = name2.upper()

    score1 = 0
    score2 = 0

    for n1 in name1:
        if n1 in true_list:
            score1 += 1

    for n2 in name2:
        if n2 in true_list:
            score1 += 1

    for n1 in name1:
        if n1 in love_list:
            score2 += 1

    for n2 in name2:
        if n2 in love_list:
            score2 += 1
    return f"{score1}{score2}"

print(calculate_love_score("Angela Yu", "Jack Bauer"))
print(calculate_love_score("Kanye West", "Kim Kardashian"))