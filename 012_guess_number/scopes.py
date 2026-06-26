enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

def increase_enemies2():
    global enemies
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
increase_enemies2()
print(f"Enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()


player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
    
    return drink_potion
    
game()()

# ----------------------
hard_enemies = 1

def increase_hard_enemies(enemy):
    print(f"enemies inside function: {hard_enemies}")
    return enemy + 1

hard_enemies = increase_hard_enemies(hard_enemies)
print(f"enemies outside function: {hard_enemies}")