def analyzer(numbers):
    numbers = numbers.split('-')
    for i, number in enumerate(numbers):
        numbers[i] = int(number)
    # tuple versie, maar dit is hoe jullie het lieten zien.
    # return {sorted(listNumbers)}', max(listNumbers), min(listNumbers), len(listNumbers), sum(listNumbers), sum(listNumbers) / len(listNumbers)
    return f'Gesorteerde list van ints: {sorted(numbers)}\nGrootste getal: {max(numbers)} en Kleinste getal: {min(numbers)}\nAantal getallen: {len(numbers)} en Som van de getallen: {sum(numbers)}\nGemiddelde: {sum(numbers) / len(numbers)}'

print(analyzer('5-9-7-1-7-8-3-2-4-8-7-9'))