def is_map_only_zero(mlist):

    count = 0
    all_zero=True
    
    for x in mlist:
        for y in x:
            if y > 0:
                count+=1
            
        
    if count > 0:
        all_zero = False
    else:
        all_zero = True
          
        
    return all_zero