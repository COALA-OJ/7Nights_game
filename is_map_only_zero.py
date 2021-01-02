import numpy as np


class is_map_only_zero:
    def __init__(self, mlist = []):
        np.sum(mlist)        
        if mlist > 0:
            all_zero=False
        else:
            all_zero=True
            
        return all_zero