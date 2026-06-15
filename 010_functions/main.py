def format_name(f_name: str, l_name: str):
    """Take a first and last name and format 
    it to return the title case version of the name."""
    print(f"{f_name.capitalize()} {l_name.title()}")

format_name("john doe", "john doe")


def funcao_1(texto):
    return texto + texto

def funcao_2(texto):
    return texto.title()

saida = funcao_2(funcao_1("python é incrível! "))

print(saida)


def name_formatter(f_name: str, l_name: str):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(name_formatter(input("What is your first name? "), input("What is your last name? ")))
