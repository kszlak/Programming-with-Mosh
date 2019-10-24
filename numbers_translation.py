dict = {'1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'}

# first solution
phone_number = input ('Please write your phone number to translate: ')
list = []
for i in phone_number:
    list.append(dict[i])

print (list)

output = ''
# better solution
for j in phone_number:
    output = (output + dict.get(j, '!!') + ' ')

print (output)

