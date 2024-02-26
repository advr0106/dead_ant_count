""" def dead_ant_count(ants):
    if ants == None:
        return 0
    
    rm_ants = ants.lower().replace('ant', '.')
    
    a_count = rm_ants.lower().count('a')
    n_count = rm_ants.lower().count('n')
    t_count = rm_ants.lower().count('t')
    
    return max(a_count, n_count, t_count) """
    
def dead_ant_count(ants):
    if ants is None:
        return 0
    
    a_count, n_count, t_count = 0, 0, 0

    i = 0
    while i < len(ants):
        if ants[i:i+3] == 'ant':
            i += 3
        else: 
            if ants[i] == 'a':
                a_count += 1
            elif ants[i] == 'n':
                n_count += 1
            elif ants[i] == 't':
                t_count += 1
            i += 1
    return max(a_count, n_count, t_count)
    




