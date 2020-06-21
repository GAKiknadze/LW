from prettytable import PrettyTable
from colorama import init,Fore
import math
import random as r
table = PrettyTable([Fore.WHITE+'НОМЕР ТЕСТА','Z1','Z2','РАВЕНСТВО'])
def Ex2(i,x,y):
    z1 = math.cos(x)**4 + math.sin(y)**2 + 0.25*math.sin(2*x)**2-1
    z2 = math.sin(y + x) * math.sin(y - x)
    if z1 == z2:
        b = Fore.LIGHTCYAN_EX+'True'+Fore.WHITE
    else:
        b = Fore.RED+'False'+Fore.WHITE
    table.add_row([i,z1,z2,b])

for i in range(1,6):
    Ex2(i,r.random(),r.random())
print(table)