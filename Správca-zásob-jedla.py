import os

SUBOR_ZASOB = "sklad.txt"


def nacitaj_sklad():
    if os.path.exists(SUBOR_ZASOB):
        novy_sklad = {}
        with open(SUBOR_ZASOB, "r", encoding="utf-8") as f:
            for riadok in f:
                riadok = riadok.strip()
                if not riadok:
                    continue
                nazov, pocet_str = riadok.split(":")
                novy_sklad[nazov] = int(pocet_str)
        return novy_sklad
    else:
       
        return {
            "Muka": 5,
            "Cukor": 3,
            "Olivovy olej": 2,
            "Ryža": 4,
            "Cestoviny": 6,
            "Tuniak": 8,
            "Mlieko": 10,
            "Paradajkovy pretlak": 7,
            "Mleta kava": 3,
            "Vajcia": 12
        }

def uloz_sklad(data):
    with open(SUBOR_ZASOB, "w", encoding="utf-8") as f:
        for polozka, pocet in data.items():
            f.write(f"{polozka}:{pocet}\n")


sklad = nacitaj_sklad()

print(" SPRÁVCA-ZÁSOB-POTRAVÍN ")

while True:
    print("\n-- MENU --")
    print("1. Zobraziť zásoby")
    print("2. Pridať položku / zvýšiť počet")
    print("3. Odobrať položku / znížiť počet")
    print("4. Koniec")

    volba = input("\nVyber si možnosť (1-4): ").strip()

    if volba == "1":
        print("\n-- Aktuálny stav na sklade --")
        if not sklad:
            print("Sklad je prázdny.")
        else:
            for polozka, pocet in sklad.items():
                print(f"- {polozka}: {pocet} ks")
                
    elif volba == "2":
        nazov = input("\n Zadaj názov ingrediencie: ").strip()
        if not nazov:
            print("Chyba:Musíš zadať nejaký názov")
            continue
            
        try:
            pocet = int(input(f"Koľko kusov '{nazov}' chceš pridať?: "))
            if pocet < 0:
                print("Chyba:Nemôžeš pridať mínusový počet kusov")
                continue
                
            if nazov in sklad:
                sklad[nazov] += pocet
            else:
                sklad[nazov] = pocet
                
            uloz_sklad(sklad)
            print(f"Úspešne aktualizované. {nazov} má teraz {sklad[nazov]} ks.")
            
        except ValueError:
            print("Chyba: Musíš zadať celé číslo")

    elif volba == "3":
        if not sklad:
            print("\nSklad je prázdny, nemožeš nič odobrať.")
            continue
            
        nazov = input("\nZadaj názov ingrediencie, ktorú chceš odobrať: ").strip()
        
        if nazov in sklad:
            try:
                pocet = int(input(f"Koľko kusov '{nazov}' sa minulo? (Na sklade: {sklad[nazov]} ks): "))
                if pocet < 0:
                    print("Chyba: Nemôžeš odobrať mínusový počet kusov")
                    continue
                
                if sklad[nazov] - pocet < 0:
                    print(f"Chyba: Nemôžeš odobrať {pocet} ks. Na sklade máš iba {sklad[nazov]} ks.")
                else:
                    sklad[nazov] -= pocet
                    print(f"Odobrané. Nový stav pre {nazov}: {sklad[nazov]} ks.")
                    
                    if sklad[nazov] == 0:
                        del sklad[nazov]
                        print(f"Ingrediencia '{nazov}' sa minula a bola vymazaná zo skladu.")
                    
                    uloz_sklad(sklad)  
            except ValueError:
                print("Chyba: Musíš zadať celé číslo")
        else:
            print(f"Chyba: Ingrediencia '{nazov}' sa v sklade nenachádza.")

    elif volba == "4":
        print("\nKoniec programu.")
        break
    else:
        print("Zadaj celé číslo od 1 do 4.")
    
    
    