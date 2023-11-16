from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

x = PrettyTable()

x.add_column("Places", ["Coorg", "Ooty"])
x.add_column("State", ["Karnataka", "Tamilnadu"])
x.align = 'c'
#x = ColorTable(theme=Themes.OCEAN)

print(x)
