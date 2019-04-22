bill = int(input('Enter total bill amount ') 
ran = input('How was your service (good, fair, bad)? ')

if (service == 'good'):
    print(bill * .20)

elif (service == 'fair'):
    print(bill * .15)

elif (service == 'bad'):
    print(bill * .10)

else:
    print('Enter good, fair, or bad')

ran