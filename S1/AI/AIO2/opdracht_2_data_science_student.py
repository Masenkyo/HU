import statistics
import matplotlib.pyplot as plt


"""
Oriëntatie op AI

Onderwerp: Statistiek

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
                                                                                                                # XXX>

"""
1. Implementatie mean
    Implementeer onderstaande functie om het gemiddelde van een lijst getallen te berekenen.
"""

def mean(lst):
    """
    Bepaalt het gemiddelde van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het gemiddelde van de gegeven getallen.
    """
    return sum(lst) / len(lst)

def median(lst):
    sort = sorted(lst)
    aantal = len(sort)
    mid = aantal // 2
    if aantal % 2 == 0:
        return (sort[mid - 1] + sort[mid]) / 2
    return float(sort[mid])
"""
2. Implementatie q1
    Implementeer onderstaande functie om het eerste kwartiel van een lijst getallen te berekenen.
    Hint: maak gebruik van `median()` uit statistiek_student.py (ja, deze mag je dus importeren)
"""

def q1(lst):
    """
    Bepaalt het eerste kwartiel - Q1 - van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het eerste kwartiel Q1 van de gegeven getallen.
    """
    sort = sorted(lst)
    aantal = len(lst)
    bottom = sort[:aantal // 2]
    return median(bottom)

"""
3. Implementatie q3
    Implementeer onderstaande functie om het derde kwartiel van een lijst getallen te berekenen.
    Hint: maak gebruik van `median()` uit statistiek_student.py (ja, deze mag je dus importeren)
"""

def q3(lst):
    """
    Bepaalt het eerste kwartiel - Q3 - van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het eerste kwartiel Q3 van de gegeven getallen.
    """
    sort = sorted(lst)
    aantal = len(sort)
    mid = aantal // 2
    top = sort[mid + 1:] if aantal % 2 != 0 else sort[mid:]
    return median(top)

"""
4. Implementatie stdev
    Implementeer onderstaande functie om de standaarddeviatie van een lijst getallen te berekenen.
    Hint: maak gebruik van `mean()` uit bovenstaande vraag.
"""

def stdev(lst):
    """
    Berekent de standaarddeviatie van een lijst met getallen.

    Parameters:
        lst (list): Een lijst met numerieke waarden.

    Returns:
        float: De standaarddeviatie van de lijst.
    """

    mien = mean(lst)
    result = sum((_ - mien) ** 2 for _ in lst) / len(lst)
    return result ** 0.5

"""
5. Implementatie iqr
    Implementeer onderstaande functie om de interkwartielafstand van een lijst getallen te berekenen.
"""

def iqr(lst):
    """
    Berekent de interkwartielafstand van een lijst met getallen.

    Parameters:
        lst (list): Een lijst met numerieke waarden.

    Returns:
        float: De interkwartielafstand van de lijst.
    """

    return q3(lst) - q1(lst)

"""
6. Implementatie outliers
    Implementeer onderstaande functie om de outliers van een lijst getallen te berekenen. Maak gebruik van de methode 
    uit de slides. 
    Hint: maak gebruik van `iqr()`uit de bovenstaande vraag.
"""

def outliers(lst):
    """
    Bepaalt de statistische uitschieters van een lijst met getallen.

    Args:
        lst (list): Een lijst met getallen.

    Returns:
        list: Een lijst met alle uitschieters van de gegeven getallen.
    """

    interKwartielAfstand = iqr(lst)
    lower = q1(lst) - 1.5 * interKwartielAfstand
    upper = q3(lst) + 1.5 * interKwartielAfstand
    return [_ for _ in lst if _ < lower or _ > upper]

"""
7. Implementatie z_scores
    Implementeer onderstaande functie om de z-scores van een lijst getallen te berekenen, volgens onderstaande pseudocode:
    1.	Onvang een lijst lst
    2.	Bereken m = gemiddelde van lst
    3.	Bereken s = stdev van lst
    4.	z_scores = lege lijst
    5.	Loop over elk element e in lst
        i.	 Bereken d = e - m
        ii.	 Bereken z = d / s
        iii. Voeg z toe aan z_scores
    f.	Retourneer z_scores
"""

def z_score(lst):
    """
    Bepaalt de z-scores van een lijst volgens de volgende pseudocode:

    Args:
        lst: Een lijst met gehele getallen.

    Returns: list met z-scores
    """
    mien = mean(lst)
    standaardDeviatie = stdev(lst)
    return [(_ - mien) / standaardDeviatie for _ in lst]

"""
8. Implementatie plot_grades
    Implementeer onderstaande functie om het gemiddelde eindcijfer t.o.v. de gemiddelde aanwezigheid te plotten in een staafdiagram.
    - Toon een x- en een y-label
    - Toon een grafiektitel (dit heb je nog nooit hoeven doen en zul je zelf moeten uitzoeken) 
"""
def plot_grades(presence, grade):
    """
    Plot het gemiddelde eindcijfer t.o.v. de gemiddelde aanwezigheid te plotten in een staafdiagram. 

    Args:
        presence (list): Een lijst met gehele getallen.
        grade (list): Een lijst met kommagetallen.
    """
    plt.bar(presence, grade)
    plt.show()

"""
9. Implementatie cumulatieve_frequenties (Optioneel)
    Implementeer onderstaande functie om de cumulatieve frequenties van een lijst getallen te berekenen.
"""

def cumulatieve_frequenties(lst):
    """
        Berekent de cumulatieve frequenties van een lijst.

        Parameters:
            lst (list): Een lijst met numerieke waarden.

        Returns:
            dict: Een dictionary waarin elke unieke waarde gekoppeld is aan diens cumulatieve frequentie.
        """
    
    return None

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random
import numpy as np
import os

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
    elif type(expected_output) is list:
        for i in range(len(expected_output)):
            if type(expected_output[i]) is float:
                # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
                assert round(output[i] - expected_output[i], 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    for _ in range(10):
        lst_test = random.choices(range(-99, 100), k=6)
        test_mean = statistics.mean(lst_test)
        __my_assert_args(mean, (lst_test,), test_mean, False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 1.5),

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 4.0),

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])



def test_stdev():
    for _ in range(10):
        test_lst = random.choices(range(-99, 100), k=9)
        test_std = statistics.pstdev(test_lst)
        __my_assert_args(stdev, (test_lst,), test_std, False)


def test_iqr():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 2, 4, 1],), 4.0),
        (([5, 7, 4, 4, 6, 2, 8],), 3.0),
        (([0, 5, 5, 6, 7, 7, 12],), 2.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 3.0),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 9.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 13.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 2.5),

    ]
    for case in testcases:
        __my_assert_args(iqr, case[0], case[1])

def test_outliers():
    testcases = [
        (([10, 100, 102, 104, 110, 120, 130, 140, 200],), [10, 200]),
        (([1, 2, 3, 4, 5, 6, 7, 8, 25],),[25]),
        (([10, 12, 12, 13, 13, 14, 15, 25, 30, 50, 0],), [50]),
        (([1, 1, 1, 2, 2, 3, 4, 5, 9, 30],), [30]),
        (([10, 11, 12, 13, 14, 15, 16, 5, 3, 25, 50],), [50])
        ]

    for case in testcases:
        __my_assert_args(outliers, case[0], case[1])

def test_z_score():
    testcases = [
        (([1, 2, 3, 4, 5, 6, 7],), [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]),
        (([-1.463, -0.878, -0.293, 0.293, 0.878, 1.463, 2.048], ), [-1.4999389387753578, -1.0001220330641452, -0.5003051273529328, 0.00036616623129023194, 0.5001830719425027, 0.999999977653715, 1.4998168833649272]),
        (([100, 101, 102, 105, 110], ), [-0.9969277961190788, -0.7200034083082231, -0.44307902049736747, 0.3876941429351995, 1.7723160819894777]),
        (([5, 8, 12, 15, 20, 25], ), [-1.3446669139174723, -0.9045941057262995, -0.3178303614714025, 0.1222424467197703, 0.8556971270383916, 1.589151807357013]),
        (([50, 60, 70, 80, 90, 100], ), [-1.4638501094227996, -0.8783100656536798, -0.2927700218845599, 0.2927700218845599, 0.8783100656536798, 1.4638501094227996])
    ]

    for case in testcases:
        __my_assert_args(z_score, case[0], case[1])


def test_cumulatieve_frequenties():
    testcases = [
        (([1, 2, 1, 5, 6, 8, 1, 5],), {1: 3, 2: 4, 5: 6, 6: 7, 8: 8}),
        (([5, 2, 6, 8, 1, 3, 2, 1, 5, 6, 7],), {1: 2, 2: 4, 3: 5, 5: 7, 6: 9, 7: 10, 8: 11}),
        (([5, 2, 6, 8, 1, 3, 2, 1, 5],), {1: 2, 2: 4, 3: 5, 5: 7, 6: 8, 8: 9}),
        (([5, 4, 3, 4, 7, 3, 2, 6, 4, 8, 9, 7],), {2: 1, 3: 3, 4: 6, 5: 7, 6: 8, 7: 10, 8: 11, 9: 12})
    ]
    for case in testcases:
        __my_assert_args(cumulatieve_frequenties, case[0], case[1])


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur

        test_id()
        test_mean()
        print("Je functie mean(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_stdev()
        print("Je functie stdev(lst) werkt goed!")

        test_iqr()
        print("Je functie iqr(lst) werkt goed!")

        test_outliers()
        print("Je functie outliers(lst) werkt goed!")

        test_z_score()
        print("Je functie z_score(lst) werkt goed!")
        
        plot_grades([29, 36, 41, 45, 48, 50, 56, 61, 67, 67, 67, 71, 75, 79, 83, 88], [4.1, 4.3, 4.0, 5.2, 4.8, 4.9, 5.9, 5.2, 4.9, 5.7, 6.2, 6.1, 4.4, 6.1, 6.8, 6.9])
        print("Je functie plot_grades faalt niet!")

        print("Optioneel:")
        test_cumulatieve_frequenties()
        print("Je functie cumulatieve_frequenties(lst) werkt goed!")

        print(f"\nGefeliciteerd {naam}, alles lijkt te werken!")
        print("\x1b[38;5;208m")
        print("Echter, test dit testframework niet of je de juiste plot bij vraag 8 hebt gemaakt.\x1b[0m")
        print("Controleer dus nog even of je plot correct is en lever dan pas je werk in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
