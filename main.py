def policz_sylaby(slowo):
    samogloski = "aeiouyąęóAEIOUYĄĘÓ"
    licznik = 0
    poprzednia_samogloska = False

    for litera in slowo:
        if litera in samogloski:
            if not poprzednia_samogloska:
                licznik += 1
                poprzednia_samogloska = True
        else:
            poprzednia_samogloska = False

    return max(licznik, 1)

def policz_slowa(zdanie):
    slowa = zdanie.strip().split()
    if not slowa:
        print("To nie jest zdanie")
        return 1
    return len(slowa)

slowo = input("Podaj słowo(word): ")
print(f"{policz_sylaby(slowo)} sylables")

zdanie = input("Podaj zdanie(sentence): ")
print(f"{policz_slowa(zdanie)} words")
