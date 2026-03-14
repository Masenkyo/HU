def namen():
    result = {}
    while True:
        naam = input('naam: ')
        if naam == '':
            break
        result[naam] = result.get(naam, 0) + 1
    print(result)
namen()