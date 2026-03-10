def analyzer(numbers):
    return f'Gesorteerde list van ints: {sorted(numbers.split('-'))}', len(numbers)


print(analyzer('5-9-7-1-7-8-3-2-4-8-7-9'))