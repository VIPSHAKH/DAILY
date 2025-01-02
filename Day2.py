import random
def oyin():
    son = random.randint(1, 10)
    taxmin = 0
    urinishlar = 0

    print("1 dan 10 gacha son o'yladim. Uni topishga harakat qiling!")

    while taxmin != son:
        taxmin = int(input("Sonni kiriting: "))
        urinishlar += 1

        if taxmin < son:
            print("Kiritilgan son kichikroq.")
        elif taxmin > son:
            print("Kiritilgan son kattaroq.")
        else:
            print(f"Tabriklayman! Siz {urinishlar} urinishda topdingiz.")

oyin()