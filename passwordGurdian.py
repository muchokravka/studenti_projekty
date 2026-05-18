heslo = input("Zadaj heslo: ")
posun = int(input("Zadaj posun: "))

male = False
velke = False
cislo = False
special = False

for znak in heslo:
    if znak.islower():
        male = True

    if znak.isupper():
        velke = True

    if znak.isdigit():
        cislo = True

    if not znak.isalnum():
        special = True

body = 0 

if len(heslo) >= 8: 
    body += 1 
if male: 
    body +=  1 
if velke:
    body += 1 
if cislo:
    body += 1
if special:
    body += 1 

if body <= 2:
    sila = "slabé"
elif body <= 4:
    sila = "stredné"
else:
     sila = "silné"

zasifrovane = ""

for znak in heslo: 
    if znak.isupper(): 
        novy = chr((ord(znak) - 65 + posun) % 26 + 65)
        zasifrovane += novy
    elif znak.islower(): 
         novy = chr((ord(znak) - 97 + posun) % 26 + 97)
         zasifrovane += novy
    else:
        zasifrovane += znak

desifrovanie = ""

for znak in zasifrovane:                       
    if znak.isupper():                         
        novy = chr((ord(znak) - 65 - posun) % 26 + 65)   
        desifrovanie += novy
    elif znak.islower():                       
        novy = chr((ord(znak) - 97 - posun) % 26 + 97)
        desifrovanie += novy
    else:
        desifrovanie += znak 

print("Povodne heslo: ", heslo)
print("Sila hesla: ", sila)
print("Zasifrovane heslo:", zasifrovane)
print("Desifrovane heslo: ", desifrovanie)