def diagnose(tep, tlak, teplota):
    if teplota > 38 and tep > 100:
        return "Horúčka a stres"
    elif tlak < 90:
        return "Nízky tlak – treba infúziu"
    else:
        return "Vitálne funkcie v poriadku"
 
 
def analyze_measurements(measurements):
    priemerny_tep = sum(m[0] for m in measurements) / len(measurements)
    if 60 <= priemerny_tep <= 100:
        hodnotenie = "v norme"
    else:
        hodnotenie = "mimo normy"
    return priemerny_tep, hodnotenie
 
 
merania = []
 
for i in range(1, 6):
    print(f"\nMeranie #{i}")
    tep = float(input("Tep (bpm): "))
    tlak = float(input("Krvný tlak (mmHg): "))
    teplota = float(input("Teplota (°C): "))
 
    vysledok = diagnose(tep, tlak, teplota)
    print(f"Diagnóza: {vysledok}")
 
    merania.append((tep, tlak, teplota))
 
priemerny_tep, hodnotenie = analyze_measurements(merania)
print(f"\nPriemerný tep po 5 meraniach: {priemerny_tep:.1f} bpm — {hodnotenie}")
 