#!/usr/bin/env python
# -*- coding=utf-8 -*-


import numpy as np


def calc_cummulative_dist(dataArray):
    """
    Description:
        Calculated the cumulative distribution from a data array without using 
        binning.  This provides a more robust way to representing the statistics
        of the incoming data without worrying about the binning/samping effect.
    
    args:
        dataArray:  1D np.array | pd.DataFrame
            1-D numpy array or dataFrame (when label is provided)
        label:      [ None | str ]
            column label for analyzed data
        steps:      [ None | int ]

    returns:
        pltX:  1D np.array
            plt data along x (data direction)
        pltY:  1D np.array
            plt data long y (density direction)
    """
    pass       
    