import prettytable

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokeman name",["pikachu", "squirte","charmander"])
table.add_column("Type",["Electric","water","Fire"])
table.align = "l"
print(table)
