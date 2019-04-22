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
