def hoogvliegers(dict_studenten_cijfers):
    result = {}
    for naam, cijfer in dict_studenten_cijfers.items():
        if cijfer > 9:
            result[naam] = cijfer
    return result
print(hoogvliegers({'gerrit':10, 'gerard':7, 'michael jackson':5, 'kanye west':3, 'sil':10}))