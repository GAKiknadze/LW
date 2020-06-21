import random
from colorama import init,Fore,Back
init(autoreset=True)
def kube(k1,k2,k3,k4,k5,k6,k7,k8,k9):

    print(Fore.WHITE+' +---------+\n',Fore.WHITE+'| {}  {}  {} '.format(k1,k2,k3)+Fore.WHITE+'|\n',Fore.WHITE+'| {}  {}  {} '.format(k4,k5,k6)+Fore.WHITE+'|\n',Fore.WHITE+'| {}  {}  {} '.format(k7,k8,k9)+Fore.WHITE+'|\n',Fore.WHITE+'+---------+\n')

def logic(g):
    if g == 1:
        kube(
            ' ', ' ', ' ',
            Fore.WHITE+' ', Fore.RED+'@', Fore.WHITE+' ',
            ' ', ' ', ' '
        )
    elif g == 2:
        kube(
            Fore.RED+'@', Fore.WHITE+' ', Fore.WHITE+' ',
            ' ', ' ', ' ',
            Fore.WHITE+' ', ' ', Fore.RED+'@'
        )
    elif g == 3:
        kube(
            Fore.RED+'@', Fore.WHITE+' ', ' ',
            ' ', Fore.RED+'@', Fore.WHITE+' ',
            ' ', ' ', Fore.RED+'@'
        )
    elif g == 4:
        kube(
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@',
            ' ', ' ', ' ',
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@'
        )
    elif g == 5:
        kube(
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@',
            ' ', Fore.RED+'@', Fore.WHITE+' ',
            Fore.RED+'@', ' ', Fore.RED+'@'
        )
    elif g == 6:
        kube(
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@',
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@',
            Fore.RED+'@', Fore.WHITE+' ', Fore.RED+'@'
        )

try:
    choose = input('Бросить игральные кости (y/n): ')
    if choose == 'y' or choose == 'Y':
        n = int(input('Введите количество игральных костей: '))
        if n<=0:
            print('Ошибка ввод недопустимых значений.')
            quit()
        for i in range(n):
            k = random.randint(1,6)
            logic(k)
    elif choose == 'n' or choose == 'N':
        quit()
    else:
        raise Exception
except (ValueError,Exception):
    print('Ошибка ввода!!!')
