def imprimir_tabela(cabecalhos, linhas):
    # 1. Descobre a largura necessária para cada coluna
    larguras = []

    for i, cabecalho in enumerate(cabecalhos):
        maior = len(str(cabecalho))

        for linha in linhas:
            tamanho = len(str(linha[i]))
            maior = max(maior, tamanho)

        larguras.append(maior)

    # 2. Cria a linha divisória
    separador = "+" + "+".join(
        "-" * (largura + 2) for largura in larguras
    ) + "+"

    # 3. Cria uma linha com os valores alinhados
    def formatar_linha(valores):
        return "|" + "|".join(
            f" {str(valor):<{largura}} "
            for valor, largura in zip(valores, larguras)
        ) + "|"

    # 4. Imprime a tabela
    print(separador)
    print(formatar_linha(cabecalhos))
    print(separador)

    for linha in linhas:
        print(formatar_linha(linha))

    print(separador)


# Exemplo de utilização
cabecalhos = ["Pokemon Name", "Type", "Color"]

linhas = [
    ["Pikachu", "Electric", "Yellow"],
    ["Squirtle", "Water", "Blue"],
    ["Charmander", "Fire", "Red"],
]

imprimir_tabela(cabecalhos, linhas)
