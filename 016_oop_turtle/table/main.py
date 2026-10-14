from table import TextTable

table = TextTable(
    headers=["Pokemon Name", "Type", "Color"],
    alignments=["left", "center", "center"]
)

table.add_row(["Pikachu", "Electric", "Yellow"])
table.add_row(["Squirtle", "Water", "Blue"])
table.add_row(["Charmander", "Fire", "Red"])

print(table)