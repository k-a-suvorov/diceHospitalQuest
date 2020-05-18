import random
from time import sleep
import os
import sys
import colorama
from colorama import Fore, Style

import source.textdef

colorama.init()

diseases = [
    'Грипп',
    "Простуда",
    "Мигрень",
    "Язва желудка",
    "Камни в почках",
    "Мозгостряс",
    "Галлюцинации",
    "Гипнобред",
    "Маньяк",
    "Слабость",
    "Гайморит",
    "Инсомния"]

doctor = random.randint(1, 16)
patient = random.randint(1, 16)


def healacttion():
    global doctor
    global patient

    if doctor > patient:
        print(Fore.GREEN, Style.BRIGHT + ' ')
        print('После лечения вы чувствуете себя гораздо лучше')
        successExit()
        gameExit()
    elif doctor <= patient:
        print(Fore.RED, Style.BRIGHT + ' ')
        print('Несмотря на все усилия специалиста вамрезко становится хуже. Кажется врачи из реанимации спешат на помощь')
        source.textdef.reanimate()


def farmacy():
    source.textdef.farmacyroom()


def surgeon():
    source.textdef.farmacyroom()


def psyhiatrist():
    source.textdef.psyhoroom()


def physiotherapy():
    source.textdef.psyhoroom()


def successDiag():
    diag = random.choice(diseases)
    if diag == diseases[0] or diag == diseases[1] or diag == diseases[2]:
        farmacy()
    elif diag == diseases[3] or diag == diseases[4] or diag == diseases[5]:
        surgeon()
    elif diag == diseases[6] or diag == diseases[7] or diag == diseases[8]:
        psyhiatrist()
    elif diag == diseases[9] or diag == diseases[10] or diag == diseases[11]:
        physiotherapy()


def dieDiagPatient():
    print(Fore.RED, Style.BRIGHT + '')
    source.textdef.endquest()
    animationShut()
    clearScreen()
    sys.exit()


def diagnostic():
    print(Fore.MAGENTA, Style.BRIGHT + '')
    source.textdef.diagnosticroom()
    switch = int(input('Желаете пройти диагностику? 1 - да, 2 нет\n>>> '))
    if (switch < 1) or (switch > 2):
        errorInputMessage()
    elif switch == 2:
        dieDiagPatient()
    elif switch == 1:
        successDiag()


# Function animation Load
def animationLoad():
    start = ['З', 'а', 'г', 'р', 'у', 'ж', 'а', 'е', 'м', ' ', 'К', 'в', 'е', 'с', 'т', '.']
    print(Fore.RED + ' ')
    sleep(0.1)
    for i in range(0, len(start)):
        sleep(0.1)
        print(Fore.CYAN, Style.BRIGHT + " ", start[i], end="")


# Function animation Shutdown
def animationShut():
    start = ['В', 'ы', 'х', 'о', 'д', 'и', 'м', ' ', 'и', 'з', ' ', 'и', 'г', 'р', 'ы', '.']
    print(Fore.RED + ' ')
    sleep(0.1)
    for i in range(0, len(start)):
        sleep(0.1)
        print(Fore.RED, Style.BRIGHT + " ", start[i], end="")


# Function clear of screen
def clearScreen():
    if (os.name == 'nt'):
        sleep(2)
        os.system('cls')
    elif (os.name == 'posix'):
        sleep(2)
        os.system('clear')
    else:
        print(Fore.WHITE, Back.RED + 'Другие операционные системы не поддерживаются!')
        clearScreen()
        sys.exit()


def helpQuest():
    print('Help!')


def welcomeQuest():
    print(Fore.GREEN, Style.BRIGHT + '\nДобро пожаловать в игру \"DiceHospitalQuest\" ver. 0.1, written by Opsis')
    print()
    print(Fore.GREEN, Style.BRIGHT + '\nВы играете за пациента, который попал в больгицу и пытается вылечится. ')
    print(Fore.YELLOW, Style.BRIGHT + '\nСобытия и результат в квесте генерируются случайным образом. Наслаждайтесь!')


def gameMenu():
    clearScreen()
    print(Fore.GREEN, Style.BRIGHT + 'Добро пожаловать в меню игры. \nВыберете один из пунктов менюЖ')
    print()
    switch = int(input('1 - играть \n 2 - выход \n 3 - Помощь\n>>> '))
    if (switch < 1) or (switch > 3):
        errorInputMessage()
    elif switch == 3:
        helpQuest()
    elif switch == 2:
        confirmForExit()
    elif switch == 1:
        runQuest()


def globalswitch():
    print()
    switch = int(input('Выберете 2, что бы испугаться и убежать, \n1 - что бы согласиться с диагностикой.\n>>> '))
    if (switch < 1) or (switch > 2):
        errorInputMessage()
    elif switch == 2:
        source.textdef.reanimate()
    elif switch == 1:
        diagnostic()


def globalheal():
    print()
    switch = int(input('Врач предлагает вам лечение. Что вы решите? \n Выберете 2, что бы испугаться и убежать, \n1 - что бы согласиться с лечением.\n>>> '))
    if (switch < 1) or (switch > 2):
        errorInputMessage()
    elif switch == 2:
        source.textdef.reanimate()
    elif switch == 1:
        healacttion()


def runQuest():
    print(Fore.MAGENTA, Style.BRIGHT + " ")
    source.textdef.startquest()
    clearScreen()
    source.textdef.reception()
    source.textdef.diagnosticroom()
    diagnostic()


def confirmForExit():
    print('Вы точно хотите выйти из игры?')
    print()
    switch = int(input('Нажмите 2, что бы выйти \n1 - что бы играть.\n>>> '))
    if (switch < 1) or (switch > 2):
        errorInputMessage()
    elif switch == 2:
        gameExit()
    elif switch == 1:
        gameMenu()


def gameExit():
    print(Fore.RED, Style.BRIGHT + 'Жаль, что покидаете игру. До свидания!')
    animationShut()
    clearScreen()
    sys.exit()

def successExit():
    print(
        '''
    Через некоторое время вас выписывают из больгицы, вот только смутное ощущение,
    что астрономический счет за лечение будет преследовать вас какое-то время
    ''')


def errorInputMessage():
    print(Fore.RED, Style.BRIGHT + 'Похоже вы не можете сейчас играть, попробуйте пройти квест позже')
    sys.exit()


def printDebug():
    print(Fore.RED, Style.BRIGHT + " ")
    print(random.choice(diseases))