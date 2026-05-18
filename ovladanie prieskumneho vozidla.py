x = 0
y = 0

def pohni_rover(smer):
    global x, y

    if smer == "vpred":
        y = y + 1
    elif smer == "vzad":
        y = y - 1
    elif smer == "vlavo":
        x = x - 1
    elif smer == "vpravo":
        x = x + 1
    else:
        print("Neznamy prikaz: " + smer)
        return

    print("Aktualna poloha: [" + str(x) + ", " + str(y) + "]")

    # BONUS: krater na [5, 5]
    if x == 5 and y == 5:
        print("HAVARIA! Rover vstupil do kratera na [5, 5]! Koniec.")
        exit()


# --- MAIN ---
print("Rover startuje na pozicii [0, 0]")
print("Prikazy: vpred, vzad, vlavo, vpravo, koniec")

while True:
    prikaz = input("\nZadaj prikaz: ")

    if prikaz == "koniec":
        print("Misia ukoncena. Rover stoji na [" + str(x) + ", " + str(y) + "]")
        break

    pohni_rover(prikaz)
    