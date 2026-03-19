import random
wordList = 'woordenlijst.txt'
def main():
    keuze = input('1. Speel galgje\n2. Verwijder een woord uit de woordenlijst\n3. Voeg woord toe aan de woordenlijst\n4. Toon aantal woorden in de woordenlijst\n5. Stoppen\n')
    match keuze:
        case '1':
            speelSessie()
            main()
        case '2':
            print('')
        case '3':
            addWord()
            main()
        case '4':
            print('')
        case '5':
            print('')

def kiesWoord(woordenDict, moeilijkheidsgrade):
    result = []
    with open(wordList, 'r') as woorden:
        for woord in woorden.readlines():
            woord.strip()
            result.append(woord)
        gekozenWoord = result[random.randint(0, len(result)-1)]
        print(len(result)-1)
    return

def speelSessie():
    kiesWoord(1, input('moeilijkheidsgrade (1 easy, 2 medium, 3 hard): '))
    attempts = 10

    return

def addWord():
    with open(wordList, 'a') as woorden:
        woorden.write(f'{input('Voeg woord toe: ')}\n') and print('New word has been added!')






if __name__ == '__main__':
    main()
