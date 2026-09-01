def binarySearch(sortedList, targetVal, attempts):
    left = 0
    right = len(sortedList) - 1

    while left <= right:
        attempts += 1
        mid = (left + right) // 2

        if sortedList[mid] == targetVal:
            return [mid, attempts]

        if sortedList[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
chosenNumber = int(input('choose number'))
attempts = 0

result = binarySearch(list, chosenNumber, attempts)

if result != -1:
  print(f"Found at index {result[0]} and it needed {result[1]} attempts")
else:
  print("Not found")