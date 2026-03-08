def prettyPrint():
    textFile = open('oefening_5_2_kaartnummers.txt', 'r')
    text = textFile.read().replace('\n', ', ').split(', ')
    print(text)
    for i in [0,2,4,6,8,10]:
        print(f'{text[i+1]} heeft kaartnummer: {text[i]}')

prettyPrint()