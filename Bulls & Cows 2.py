import random

# 1.Program pozdraví užitele a vypíše úvodní text
oddelovac = "_" * 47

print("Hi there!", oddelovac, sep='\n')
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac, "Enter a number:", oddelovac, sep='\n')

heslo = []
pokus = 0

# 2.Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
def tajny_kod():
    for cislo in range(4):
        x = random.randrange(0,10)
        heslo.append(x)
    if len(heslo) > len(set(heslo)):     # kontrola delky v setu (neopakuji se tam cislice, zajisteni 4 ruznych cisel)
        heslo.clear()
        tajny_kod()
    if heslo[0] == 0:                   # kontrola prvni honoty, aby nebyla 0
        heslo.clear()
        tajny_kod()
#tajny_kod()
#print(heslo)


def hlavni_hra():
    global pokus
    pokus += 1
    vyber = input(">>>")
    if vyber.isdigit() and len(vyber) == 4:          # kontrola vstupu
        vyber = vyber
    elif vyber[0] == 0:
        print("The first number is not a 0!")
    else:
        print("Selection is not a 4 digit number")
        hlavni_hra()
    vyber_lst = [int(x) for x in str(vyber)]  # prevod na list
    if vyber_lst[0] == 0:
        print("The first number is not a 0")
        hlavni_hra()
    elif len(set(vyber)) != 4:
        print("The numbers must be different!")
        hlavni_hra()
    bulls = 0
    cows = 0
    hrac = []
    for i in range(4):
        hrac.append(vyber_lst[i])
    for a in range(4):
        if hrac[a] == heslo[a]:
            bulls += 1
    for i in range(4):
        for j in range(4):
            if hrac[i] == heslo[j] and hrac[i] != heslo[i]:
                cows += 1


    #ohled na jednotné a množné číslo
    if bulls == 1:
        print("Bull: ", bulls)
    else:
        print("Bulls: ", bulls)
    if cows == 1:
        print("Cow: ", cows)
    else:
        print("Cows: ", cows)


    if bulls == 4:
        print("Correct, you've guessed the right number")
        print("in", pokus, "guesses!")
        print(oddelovac)
        quit()
    if bulls != 4:
        hlavni_hra()

tajny_kod()
print(heslo)
hlavni_hra()

