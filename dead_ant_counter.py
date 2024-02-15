def dead_ant_count(ants):
    if ants == None:
        return 0
    
    rm_ants = ants.lower().replace('ant', '.')
    
    a_count = rm_ants.lower().count('a')
    n_count = rm_ants.lower().count('n')
    t_count = rm_ants.lower().count('t')
    
    return max(a_count, n_count, t_count)
    