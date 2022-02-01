import random

# 1.Program pozdraví užitele a vypíše úvodní text
def pozdrav():
    oddelovac = "_" * 47

    print("Hi there!", oddelovac, sep='\n')
    print("""I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.""")
    print(oddelovac, "Enter a number:", oddelovac, sep='\n')

pokus = 0

# 2.Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
def tajny_kod():
    heslo = []
    for cislo in range(4):
        x = random.randrange(0, 10)
        heslo.append(x)
    if len(heslo) > len(set(heslo)):  # kontrola delky v setu (neopakuji se tam cislice, zajisteni 4 ruznych cisel)
        heslo.clear()
        heslo = tajny_kod()
    elif heslo[0] == 0:  # kontrola prvni honoty, aby nebyla 0
        heslo.clear()
        heslo = tajny_kod()
    return heslo

# 3.hlavní hra
def hlavni_hra(heslo):
    global pokus
    pokus += 1
    vyber = input(">>>")
    if vyber.isdigit() and len(vyber) == 4:  # kontrola vstupu
        vyber = vyber
    else:
        print("Selection is not a 4 digit number")
        hlavni_hra(heslo)
    vyber_lst = [int(x) for x in str(vyber)]  # prevod na list
    if vyber_lst[0] == 0:
        print("The first number is not a 0")
        hlavni_hra(heslo)
    elif len(set(vyber)) != 4:
        print("The numbers must be different!")
        hlavni_hra(heslo)
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
    mnozne(bulls, cows)
    game_over(bulls, heslo)

# ohled na jednotné a množné číslo
def mnozne(bulls, cows):
    oddelovac = "_" * 47
    if bulls == 1:
        print("Bull: ", bulls)
    else:
        print("Bulls: ", bulls)
    if cows == 1:
        print("Cow: ", cows)
    else:
        print("Cows: ", cows)
    print(oddelovac)


# rozhodnutí o konci hry
def game_over(bulls, heslo):
    oddelovac = "_" * 47
    if bulls == 4:
        print("Correct, you've guessed the right number")
        print("in", pokus, "guesses!")
        print(oddelovac)
        quit()
    else:
        hlavni_hra(heslo)


def main():
    pozdrav()
    heslo = tajny_kod()
    print(heslo)
    hlavni_hra(heslo)


if __name__ == "__main__":
    main()