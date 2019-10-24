# convertion to emoji icons
def emoji_conv(message):
    list = message.split(' ')
    dict = {
        ':)': '😊',
        ':(': '😒'
    }
    output = ''
    for i in list:
        output = output + dict.get(i, i) + ' '
    return output


message = input('> ')
print(emoji_conv(message))