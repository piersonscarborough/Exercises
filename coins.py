coin_count = -1


user_coins = "yes"

while user_coins == "yes":
    coin_count += 1
    print('You have %d coins' % (coin_count))
    user_coins = input('Do you want another? ')
print('bye')
