import mad_lib_generator

want_to_write_a_madLib = 'yes'

while (want_to_write_a_madLib == 'yes'):
    adj = input('Please provide an adjective ')
    noun = input('Please provide a noun ')
    num = int(input('Please provide a number '))
    print(mad_lib_generator.makeMadLib(adj, noun, num))
    want_to_write_a_madLib = input('Would you like to play again? ')
    



