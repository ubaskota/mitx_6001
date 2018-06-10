def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    
    
    small = 0
    big = small +1 
    
    while(small < big):
        
        diff1 = abs(num - base ** small)
        diff2 = abs(num - base ** big)
        
        if (diff1 < diff2):
            return small
            break
        
        elif (diff2 < diff1):
            small = big
            big = small + 1