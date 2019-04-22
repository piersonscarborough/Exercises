sentence = 'I LIKE FOOD'

new_string = ""

for letter in sentence:
    if letter == 'I':
        new_string += '1'
    elif letter == 'O':
        new_string += '0'
    elif letter == 'E':
        new_string += '3'
    else:
        new_string += letter

print(new_string)
