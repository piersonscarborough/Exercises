sentence = 'spooon'

new_string = ""

for i in range(len(sentence)):
    #print(sentence[i])
    if(i < len(sentence)-1):
        if sentence[i] == sentence[i+1]:
            print(sentence[i])

        '''

        new_string += 'OOOOO'
    elif letter == 'U':
        new_string += 'UUUUU'
    elif letter == 'E':
        new_string += 'EEEEEE'
    elif letter == 'A':
        new_string += 'AAAAA'
    else:
        new_string += letter
        '''
print(new_string)