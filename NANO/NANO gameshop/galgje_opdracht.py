import random
import os

def lees_woorden(bestandsnaam):
    """
    Leest alle woorden uit het woordenbestand en returnt een dictionary 
    waarin het woord en diens moeilijkheid staat.
    """
    woorden_dict = {}
    if not os.path.exists(bestandsnaam):
        return woorden_dict
        
    with open(bestandsnaam, 'r') as f:
        for line in f:
            woord = line.strip().lower()
            if woord:
                lengte = len(woord)
                if lengte <= 6: # Inclusief 6 om het gat in de opdracht te vullen
                    moeilijkheid = 1
                elif 7 <= lengte <= 11:
                    moeilijkheid = 2
                else:
                    moeilijkheid = 3
                woorden_dict[woord] = moeilijkheid
    return woorden_dict

def sla_woorden_op(bestandsnaam, woorden_dict):
    """
    Schrijft de volledige woordenlijst terug naar het bestand.
    """
    with open(bestandsnaam, 'w') as f:
        for woord in woorden_dict:
            f.write(f"{woord}")

def bereken_score(aantal_levens_over, moeilijkheid):
    """
    Berekent de score: aantal_levens_over * moeilijkheid.
    """
    return aantal_levens_over * moeilijkheid

def voeg_score_toe(naam, woord, score):
    """
    Voegt score van gebruiker toe aan het bestand 'scores.txt'.
    """
    with open("scores.txt", "a") as f:
        f.write(f"Naam: {naam}, Woord: {woord}, Score: {score}")

def toon_tussenstand(woord, geraden_letters):
    """
    Toont de geraden letters als volgt V _ _ R _ E E L D.
    """
    resultaat = []
    for letter in woord:
        if letter in geraden_letters:
            resultaat.append(letter.upper())
        else:
            resultaat.append("_")
    
    geformatteerd = " ".join(resultaat)
    print(geformatteerd)
    return geformatteerd

def kies_woord(woorden_dict, moeilijkheidsgraad):
    """
    Returnt een random gekozen woord met de meegegeven moeilijkheidsgraad.
    """
    mogelijke_woorden = [w for w, m in woorden_dict.items() if m == moeilijkheidsgraad]
    if not mogelijke_woorden:
        return None
    return random.choice(mogelijke_woorden)

def speel_sessie():
    """
    Behandelt een volledige speelsessie van Galgje.
    """
    naam = input("Je naam: ")
    woorden_dict = lees_woorden("woordenlijst.txt")
    
    if not woorden_dict:
        print("De woordenlijst is leeg! Voeg eerst woorden toe.")
        return

    try:
        moeilijkheid = int(input("Kies een moeilijkheid (1=makkelijk, 2=normaal, 3=moeilijk): "))
    except ValueError:
        print("Ongeldige invoer, we kiezen moeilijkheid 1.")
        moeilijkheid = 1

    woord = kies_woord(woorden_dict, moeilijkheid)
    if not woord:
        print(f"Geen woorden gevonden voor moeilijkheid {moeilijkheid}.")
        return

    # Levens bepalen op basis van moeilijkheid
    levens = {1: 10, 2: 8, 3: 6}.get(moeilijkheid, 10)
    
    geraden_letters = set()
    foutieve_letters = set()
    woord_letters = set(woord)
    
    print(f"Woord gekozen (moeilijk {moeilijkheid}): {'_ ' * len(woord)}(lengte {len(woord)}, levens: {levens})")

    while levens > 0:
        poging = input("Raad een letter (Enter om te stoppen): ").lower().strip()
        
        if not poging:
            print("Sessie afgebroken.")
            return

        if len(poging) > 1:
            print("Voer a.u.b. maar één letter tegelijk in.")
            continue

        if poging in geraden_letters or poging in foutieve_letters:
            print(f"Letter '{poging}' is al geraden. Geen levensverlies.")
            continue

        if poging in woord_letters:
            geraden_letters.add(poging)
            print("Goed!", end=" ")
            toon_tussenstand(woord, geraden_letters)
            
            if geraden_letters == woord_letters:
                score = bereken_score(levens, moeilijkheid)
                print(f"Gefeliciteerd! Je hebt het woord '{woord.upper()}' geraden.")
                print("--- Sessie resultaat ---")
                print(f"Woord: {woord} | Resultaat: WIN")
                print(f"Levens resterend: {levens}")
                print(f"Score: {score}")
                voeg_score_toe(naam, woord, score)
                return
        else:
            foutieve_letters.add(poging)
            levens -= 1
            print(f"Mis!", end=" ")
            toon_tussenstand(woord, geraden_letters)
            print(f"(levens: {levens}) | Foutieve letters: {', '.join(foutieve_letters)}")

    print(f"Helaas, je levens zijn op. Het woord was: {woord.upper()}")
    voeg_score_toe(naam, woord, 0)

def main():
    while True:
        print("=== Galgje Controller ===")
        print("1. Speel galgje")
        print("2. Verwijder een woord uit de woordenlijst")
        print("3. Voeg woord toe aan de woordenlijst")
        print("4. Toon aantal woorden in de woordenlijst")
        print("5. Stoppen")
        
        keuze = input("Kies een optie: ").strip()
        
        if keuze == '1':
            speel_sessie()
        elif keuze == '2':
            bestandsnaam = "woordenlijst.txt"
            woorden_dict = lees_woorden(bestandsnaam)
            woord_te_verwijderen = input("Welk woord wil je verwijderen? ").lower().strip()
            if woord_te_verwijderen in woorden_dict:
                del woorden_dict[woord_te_verwijderen]
                sla_woorden_op(bestandsnaam, woorden_dict)
                print(f"Woord '{woord_te_verwijderen}' is verwijderd.")
            else:
                print("Dit woord staat niet in de lijst.")
        elif keuze == '3':
            bestandsnaam = "woordenlijst.txt"
            woorden_dict = lees_woorden(bestandsnaam)
            nieuw_woord = input("Welk woord wil je toevoegen? ").lower().strip()
            if nieuw_woord and nieuw_woord not in woorden_dict:
                woorden_dict[nieuw_woord] = None # Wordt opnieuw berekend bij inlezen
                sla_woorden_op(bestandsnaam, woorden_dict)
                print(f"Woord '{nieuw_woord}' is toegevoegd.")
            else:
                print("Ongeldig woord of woord bestaat al.")
        elif keuze == '4':
            woorden_dict = lees_woorden("woordenlijst.txt")
            print(f"Aantal woorden in woordenbestand: {len(woorden_dict)}")
        elif keuze == '5':
            print("Tot de volgende keer!bye")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main()
