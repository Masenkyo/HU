
"""
Oriëntatie op AI

Onderwerp: Algoritmiek

(c) 2024 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)`
Veerle Hobbelink (veerle.hobbelink@hu.nl)

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Sil Wever"
klas = "R"
studentnummer = 1921198


"""
1.  Sorteeralgoritme
    Hieronder staat de pseudocode van een sorteeralgoritme:

    1. Ontvang lijst lst
    2. Herhaal voor elke index i in lst
    3.    Definieer swap_i = i
    4.    Herhaal voor elke index j in lst, startend bij i + 1
    5.        Als lst[i] > lst[j]
    6.          swap_i = swap_i + 1
    7.    Wissel lst[i] en lst[swap_i] om
    8.    Herhaal stap 3 t/m 7 totdat i == swap_i
    
    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""

# i=0: [4,3,1,2] -> swapI=3 -> wissel -> [2,3,1,4]
#       [2,3,1,4] -> swapI=1 -> wissel -> [3,2,1,4]
#       [3,2,1,4] -> swapI=2 -> wissel -> [1,2,3,4]
#       [1,2,3,4] -> swapI=0 -> klaar
# i=1: [1,2,3,4] -> swapI=1 -> klaar
# i=2: [1,2,3,4] -> swapI=2 -> klaar
# i=3: [1,2,3,4] -> swapI=3 -> klaar
# Eindresultaat: [1,2,3,4]


"""

    1b. Implementatie
            Implementeer het sorteeralgoritme in Python in een functie
            hieronder genaamd my_sort(lst).
"""

def my_sort(lst):
    """
    Hieronder staat nogmaals de pseudocode van een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:

    1. Ontvang lijst lst
    2. Herhaal voor elke index i in lst
    3.    Definieer swap_i = i
    4.    Herhaal voor elke index j in lst, startend bij i + 1
    5.        Als lst[i] > lst[j]
    6.          swap_i = swap_i + 1
    7.    Wissel lst[i] en lst[swap_i] om
    8.    Herhaal stap 3 t/m 7 totdat i == swap_i

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.
    Je moet de pseudocode volgen in je implementatie van het algoritme.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.

    """
    lst_sorted = list(lst)

    for i in range(len(lst_sorted)):
        while True:
            swapI = i
            for j in range(i + 1, len(lst_sorted)):
                if lst_sorted[i] > lst_sorted[j]:
                    swapI += 1

            lst_sorted[i], lst_sorted[swapI] = lst_sorted[swapI], lst_sorted[i]

            if i == swapI:
                break

    return lst_sorted

"""    
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 5. van de
            pseudocode) zijn nodig geweest?
"""

# Best case: [1, 2, 3] (al gesorteerd)
# i=0: j=1 (1>2? nee), j=2 (1>3? nee) -> 2 vergelijkingen
# i=1: j=2 (2>3? nee) -> 1 vergelijking
# Totaal: 3 vergelijkingen

""" 

        -   Bij welke volgorde van de waarden in de lijst is het
                    sorteeralgoritme het minst snel klaar (worst-case scenario)?
                    Hoeveel vergelijkingen zijn nodig geweest?
"""
# Worst case: [3, 2, 1] (omgekeerd gesorteerd)
# i=0 ronde 1: 3>2, 3>1 -> swapI=2, wissel -> [1,2,3] (2 vergelijkingen)
# i=0 ronde 2: 1>2? nee, 1>3? nee -> swapI=0, klaar   (2 vergelijkingen)
# i=1 ronde 1: 2>3? nee -> swapI=1, klaar              (1 vergelijking)
# Totaal: 5 vergelijkingen

"""

        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
# Best case: [1, 2, 3, 4] -> 6 vergelijkingen
# Worst case: [4, 3, 2, 1] -> 11 vergelijkingen
"""
"""

def rekenkundige_rij_recursief(start, step, length):
    """
    Berekent en retourneert het laatste element van de recursieve rij (a_n = a_n-1 + c).

    Args:
        start (int): De eerste term van de rij (a_0)
        step (int): Het verschil tussen opeenvolgende termen (c)
        length (int): De lengte van de rij (n)
    Returns:
        int: Het laatste element (a_n) van de rekenkundige rij

    """
    if length == 1:
        return start

    return rekenkundige_rij_recursief(start + step, step, length - 1)


"""
(Optioneel)
3.  Sorteeralgoritme 2
        Implementeer het sorteeralgoritme in Python in een functie hieronder 
        genaamd my_sort_2(lst).

"""

def my_sort_2(lst):
    """
     Hieronder staat de pseudocode van nog een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:
    1. Ontvang lijst lst
    2. Vind het grootste getal m in lst
    3. Maak een lijst lst_2 van lengte m+1 en vul deze met nullen
    4. Voor elke waarde w in lst:
    5.     Verhoog de waarde in lst_2 op de index w met 1
    6. Maak lege lijst lst_3
    7. Voor elke index i in lst_2
    8.     Voeg lst_2[i] keer de waarde i toe aan lst_3
    9. Retourneer lst_3

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.
    Je moet de pseudocode volgen in je implementatie van het algoritme.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    sorted_lst = []

    return sorted_lst


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""

import numpy as np
import random
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"

def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"

def test_my_sort_2():
    lst_test = random.choices(range(0, 100), k=6)
    lst_output = my_sort_2(lst_test)

    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"

def test_rekenkundige_rij_recursief():
    testcase = [
        ((1, 1, 3), 3),
        ((5, 3, 5,), 17),
        ((-1, 2, 2,), 1),
        ((5, -2, 6,), -5)

    ]

    for case in testcase:
        __my_assert_args(rekenkundige_rij_recursief, case[0], case[1])

def test_test_rekenkundige_rij_recursief_recursiveness():
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        rekenkundige_rij_recursief(1, 1, 100)
        assert False, "Fout: rekenkundige_rij_recursief werkt niet recursief"
    except RecursionError:
        return
    finally:
        sys.setrecursionlimit(limit)

def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_rekenkundige_rij_recursief()
        print("Je functie rekenkundige_rij_recursive() werkt goed!")

        test_test_rekenkundige_rij_recursief_recursiveness()
        print("Je functie rekenkundige_rij_recursive() is recursief!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("\x1b[38;5;208m")
        print("Echter, test dit testframework niet of je de pseudocode goed heb gevolgd en of je de open vragen goed hebt beantwoord.\x1b[0m")
        print("Controleer dit dus nog even en lever dan pas je werk in op Canvas...")


        print('\nOptioneel:')
        test_my_sort_2()
        print('Je functie my_sort_2() werkt goed!')


    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")  # Reset tekstkleur




if __name__ == '__main__':
    __main()
