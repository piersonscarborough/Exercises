import mad_lib_generator

want_to_write_a_madLib = 'yes'

while want_to_write_a_madLib == 'yes':
    adj = input('Please provide an adjective ')
    noun = input('Please provide a noun ')
    num = int(input('Please provide a number '))
    print(mad_lib_generator.makeMadLib(adj, noun, num))


    want_to_write_a_madLib = input('Would you like to play again? ')




def fix_adj(adj):
    upper_adj = adj.upper()
    return upper_adj

def fix_noun(noun):
    upper_noun = noun.upper()
    return upper_noun

def makeMadLib(adj, noun, num):
    adj = fix_adj(adj)
    noun = fix_noun(noun)
    madLib = 'Your rap name is %s %s and you will sell %d records' % (adj, noun, num)
    return madLib