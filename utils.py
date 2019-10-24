def find_max(numbers):
    maxim = 0
    for n in numbers:
        if n > maxim:
            maxim = n
    return maxim
