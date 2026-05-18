from users import ucty
from log import logni
from auth import hash_password
import time
from getpass import getpass
access = False
pokusy = 3
while True:
    
    while pokusy > 0 and not access:
        print("\n=== PRIHLASENIE ===")

        meno = input("Meno: ")
        heslo = hash_password(getpass("Heslo: "))

        print("\nPrihlasovanie...")

        if meno in ucty and ucty[meno] == heslo:
            access = True
            logni(meno, "Successful login")
            print("\nVstup do miestnosti s reaktorom bol povoleny")
        else:
            pokusy -= 1
            logni(meno, "Unsuccessful login")
    
    if pokusy <= 0:
        print("Varujem ta !@##@!#@#!#!#@!#@!#@!#@!#@@!#@")
        print("\tspravne heslo pis")
        print("\nmas 30 sekund timeout ")
        time.sleep(30)
        pokusy = 3
    
    if access:
        break