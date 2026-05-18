kapacity = {
    "pitná": 500,
    "úžitková": 300,
    "recyklovaná": 200
}

stav = {
    "pitná": 500,
    "úžitková": 300,
    "recyklovaná": 200
}

historia = []

def varovanie(nadrz):
    if stav[nadrz] == 0:
        print("Nádrž", nadrz, "je prázdna – odber nie je možný.")
    elif stav[nadrz] < 0.2 * kapacity[nadrz]:
        print("Varovanie: Nádrž", nadrz, "má menej ako 20 % kapacity.")

def zobraz_stav():
    print("Stav nádrží:")
    for n in stav:
        print(n, ":", stav[n], "l z", kapacity[n], "l")
        varovanie(n)

def odober_vodu():
    print("Dostupné nádrže: pitná, úžitková, recyklovaná")
    nadrz = input("Zadaj nádrž: ").strip().lower()

    if nadrz not in stav:
        print("Neznáma nádrž.")
        return

    mnozstvo = int(input("Koľko litrov chceš odobrať? "))

    if mnozstvo <= 0:
        print("Množstvo musí byť kladné.")
        return

    if stav[nadrz] == 0:
        print("Nádrž je prázdna, odber nie je možný.")
        return

    if mnozstvo > stav[nadrz]:
        print("Nedostatok vody v nádrži.")
        return

    stav[nadrz] -= mnozstvo
    historia.append("Odber " + str(mnozstvo) + " l z nádrže " + nadrz)
    print("Odobratých", mnozstvo, "l z nádrže", nadrz)
    varovanie(nadrz)

def dopln_vodu():
    print("Dostupné nádrže: pitná, úžitková, recyklovaná")
    nadrz = input("Zadaj nádrž: ").strip().lower()

    if nadrz not in stav:
        print("Neznáma nádrž.")
        return

    mnozstvo = int(input("Koľko litrov chceš doplniť? "))

    if mnozstvo <= 0:
        print("Množstvo musí byť kladné.")
        return

    if stav[nadrz] + mnozstvo > kapacity[nadrz]:
        print("Prekročenie kapacity nádrže.")
        return

    stav[nadrz] += mnozstvo
    print("Do nádrže", nadrz, "bolo doplnených", mnozstvo, "l")

def zobraz_historiu():
    print("História odberov:")
    if not historia:
        print("Zatiaľ nebol vykonaný žiadny odber.")
    else:
        for zaznam in historia:
            print(zaznam)

while True:
    print("1. Zobraziť stav nádrží")
    print("2. Odobrať vodu")
    print("3. Dopiš vodu")
    print("4. História odberov")
    print("5. Koniec")

    volba = input("Vyber možnosť: ")

    if volba == "1":
        zobraz_stav()
    elif volba == "2":
        odober_vodu()
    elif volba == "3":
        dopln_vodu()
    elif volba == "4":
        zobraz_historiu()
    elif volba == "5":
        print("Program ukončený.")
        break
    else:
        print("Neplatná voľba.")
