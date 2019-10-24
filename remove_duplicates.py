#the first method
numbers = [1, 2, 5, 1, 1, 5, 7, 8, 7, 9, 0, 0, 0, 0]

for number in numbers:
    while numbers.count(number) > 1:
        numbers.remove(number)

print (numbers)

#the better method
numbers2 = [1, 2, 5, 1, 1, 5, 7, 8, 7, 9, 0, 0, 0, 0]
unique = []

for number in numbers2:
    if number not in unique:
        unique.append(number)

print (unique)

