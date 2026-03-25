import random
import os


def Choose():
    bestandsNaam = "woordenlijst.txt"
    #region checkForFile
    # deze code staat hier om errors te voorkomen voor als er geen tekst bestand bestaat.
    if not os.path.exists(bestandsNaam):
        print(f"bestand bestaat niet")
        with open(bestandsNaam, 'w') as f:
            pass
        woordenDictionary = LeesWoord(bestandsNaam)
        nieuwWoord = input("voeg woord toe: ").lower()
        if nieuwWoord not in woordenDictionary:
            woordenDictionary[nieuwWoord] = None
            SlaWoordenOp(bestandsNaam, woordenDictionary)
            print(nieuwWoord, "is toegevoegt!")
        else:
            print("dat woord bestaat al in de woordenlijst")
        Choose()
    #endregion
    keuze = input('1. Speel galgje\n2. Verwijder een woord uit de woordenlijst\n3. Voeg woord toe aan de woordenlijst\n4. Toon aantal woorden in de woordenlijst\n5. Stoppen\n')
    match keuze:
        case '1':
            SpeelSessie()
        case '2':
            woordenDictionary = LeesWoord(bestandsNaam)
            verwijderWoord = input("verwijder woord: ").lower().strip()
            if verwijderWoord in woordenDictionary:
                del woordenDictionary[verwijderWoord]
                SlaWoordenOp(bestandsNaam, woordenDictionary)
                print(f"woord '{verwijderWoord}' is verwijderd.")
            else:
                print("Dit woord staat niet in de lijst.")
            Choose()
        case '3':
            woordenDictionary = LeesWoord(bestandsNaam)
            nieuwWoord = input("voeg woord toe: ").lower()
            if nieuwWoord not in woordenDictionary:
                woordenDictionary[nieuwWoord] = None
                SlaWoordenOp(bestandsNaam, woordenDictionary)
                print(nieuwWoord, "is toegevoegt!")
            else:
                print("dat woord bestaat al in de woordenlijst")
            Choose()
        case '4':
            print('aantal woorden in woordenlijst: ', len(LeesWoord("woordenlijst.txt")))
            Choose()
        case '5':
            print('doeg')

def LeesWoord(bestandsnaam):
    woordenDictionary = {}
    with open(bestandsnaam, 'r') as file:
        for woorden in file:
            woord = woorden.strip()
            if woord:
                lengte = len(woord)
                if lengte <= 6:
                    moeilijkheid = 1
                elif lengte <= 11:
                    moeilijkheid = 2
                else:
                    moeilijkheid = 3
                woordenDictionary[woord] = moeilijkheid
    return woordenDictionary

def KiesWoord(woordenDict, moeilijkheidsgrade):
    return random.choice([woord for woord, moeilijkheid in woordenDict.items() if moeilijkheid == moeilijkheidsgrade])

def ToonTussenstand(woord, guessedWords):
    result = []
    for letter in woord:
        if letter in guessedWords:
            result.append(letter.upper())
        else:
            result.append("_")

    tussenstand = " ".join(result)
    print(tussenstand)
    return tussenstand

def BerekenScore(aantalLevensOver, moeilijkheid):
    return aantalLevensOver * moeilijkheid

def VoegScoreToe(naam, woord, score):
    with open("scores.txt", "a") as f:
        f.write(f"naam: {naam} | woord: {woord} | score: {score}\n")

def SpeelSessie():
    naam = input("naam: ")
    try:
        moeilijkheid = int(input('moeilijkheidsgrade (1 easy, 2 medium, 3 hard): '))
    except ValueError:
        print('je voerde geen 1, 2 of 3 in, moeilijkheid woord easy')
        moeilijkheid = 1

    woordenDictionairy = LeesWoord("woordenlijst.txt")

    beschikbareWoorden = [w for w, m in woordenDictionairy.items() if m == moeilijkheid]

    if not beschikbareWoorden:
        print('er zijn geen woorden voor deze moeilijkheidsgrade, voeg woorden toe zodat je deze kan kiezen')
        return

    woord = KiesWoord(woordenDictionairy, moeilijkheid)

    attempts = 0
    levens = {1:10, 2:8, 3:6}.get(moeilijkheid)
    guessedLetters = set()
    wrongLetters = set()
    woordLetters = set(woord)

    ToonTussenstand(woord, guessedLetters)
    while levens > 0:
        guess = input('kies een letter: ').lower()

        if not guess:
            return

        if len(guess) > 1:
            print("voer aub 1 letter in")
            continue

        if guess in guessedLetters or guess in wrongLetters:
            print(f"je hebt de letter {guess} al een keer ingevoerd")
            continue

        attempts += 1
        if guess in woordLetters:
            guessedLetters.add(guess)
            print(f"{guess} zit in het woord!")
            ToonTussenstand(woord, guessedLetters)

            if guessedLetters == woordLetters:
                score = BerekenScore(levens, moeilijkheid)
                print(f"you guessed the word! {woord}\npogingen: {attempts}\nlevens: {levens}\nscore: {score}")
                VoegScoreToe(naam, woord, score)
                [SpeelSessie() if input("play again? (y/n): ") == 'y' else print("tot ziens!") and quit()]
                return
        else:
            wrongLetters.add(guess)
            levens -= 1
            ToonTussenstand(woord, guessedLetters)
            print(f"{guess} zit niet in het woord...\nlevens: {levens} | foute letters: {', '.join(wrongLetters)}")
            if levens == 0:
                print(f"het woord was {woord}")
    [SpeelSessie() if input("play again? (y/n): ") == 'y' else print("tot ziens!") and quit()]

#region comments
# als ik niet deze parameters hoefde toe te voegen was deze script echt 10 lijnen korter bruh
# ook staat er dat ik de volledige woordenlijst terug naar het bestand moet schrijven, dus ik moet letterlijk elk woord opnieuw
# erin zetten met write inplaats van append :sob:
#regionend
def SlaWoordenOp(bestandsnaam, woordenDictionary):
    with open(bestandsnaam, 'w') as woorden:
        for woord in woordenDictionary:
            woorden.write(f'{woord}\n')

if __name__ == '__main__':
    Choose()
