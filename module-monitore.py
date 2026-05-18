# Premenne a input
print ("Zadajte hladinu O2")
HladinaO2 =  int(input("Hladina O2 je: " ))
print ("Zadajte hladinu CO2")
HladinaCO2 =  float(input("Hladina CO2 je: "))
print ("Zadajte tlak v kPa: ")
Tlak =  int(input("tlak je: "))
print ("Zadajte teplotu v stupnosch C: ")
Teplota =  int(input("teplota je: "))


# Stav a varvania

Stav = ""
Varovanie = 0
Kriticky = 0
Bezpecny = 0

# O2

if HladinaO2 < 19: 
    print ("Kriticky alarm hladina kyslika je prilis nizka")
    Kriticky += 1

elif HladinaO2 > 25:
    print ("Varovanie hladina kysliku prilis vysoka riziko poziaru")
    Varovanie += 1

else:
    print ("Bezpecny stav hladina O2 je v norme")
    Bezpecny += 1
# CO2
    
if HladinaCO2 > 1:
    print ("Varvanie vysoka koncentracia CO2 , Vetrat!")
    Kriticky += 1

elif HladinaCO2 < 0.04:
    print("varovanie  CO2 je  nizke!")
    Varovanie += 1  

else:
    print ("Bezpecny stav hladina CO2 je v norme")
    Bezpecny += 1

# Tlak
    
if Tlak > 95 and Tlak < 105:
    print ("Bezpecny stav tlak je v norme")
    Bezpecny += 1

else :
    print ("Kriticky alarm tlak je nestabilny hrozi dekompresia"  )
    Kriticky += 1

# Teplota

if Teplota < 18:
    print ("Kurenie zapnute")

elif Teplota > 30:
    print ("Kurenie zapnute")

else :
    print ( "Teplota je idealna")

# Vyhodnotenie stavu modulu 

if Kriticky > Varovanie and Kriticky > Bezpecny :
     Stav = "Kriticky"
     print ("Stav monitora je: ", Stav)

elif Varovanie > Kriticky and Varovanie > Bezpecny :
     Stav = "Varovanie"
     print ("Stav monitora je: ", Stav)

elif Bezpecny > Kriticky and Bezpecny > Varovanie :
     Stav = "Bezpecny"
     print ("Stav monitora je: ", Stav)