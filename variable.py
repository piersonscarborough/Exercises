bill = int(input("Please enter bill amount: "))
service = input("How was your service? ")

if service == 'good':
    tip = bill * .20
    print('tip amount: %d' % tip)

elif service == 'fair':
    tip = bill * .15
    print('tip amount: %d' % tip)

elif service == 'bad':
    tip = bill * .20
    print('tip amount: %d' % tip)

else:
    print('Enter good, fair, or bad')