#!/usr/bin/env python
# -*- coding=utf-8 -*-


import numpy as np
import pandas as pd


def calc_cummulative_dist(data, label=None, steps=None):
    """
    description:
        Calculated the cumulative distribution from a data array without using
        binning.  This provides a more robust way to representing the statistics
        of the incoming data without worrying about the binning/samping effect.
    args:
        data:       1D np.array | full pd.DataFrame
            1-D numpy array or dataFrame (when label is provided)
        label:      [ None | str ]
            column label for analyzed data
        steps:      [ None | int ]
            Number of elements in the returning array
    returns:
        pltX:  1D np.array
            plt data along x (data direction)
        pltY:  1D np.array
            plt data long y (density direction)
    """
    if isinstance(data, pd.DataFrame):
        x = np.sort(data[label])
    else:
        x = np.sort(data)

    # check if list empty
    if len(x) < 1:
        return [], []

    # subsamping if steps is speficiied and the number is smaller than the
    # total lenght of x
    if (steps is not None) and len(x) > steps:
        x = x[np.arange(0, len(x), int(np.ceil(len(x)/steps)))]

    # calculate the cumulative density
    xx = np.tile(x, (2, 1)).flatten(order='F')
    y = np.arange(len(x))
    yy = np.vstack((y, y+1)).flatten(order='F')/float(y[-1])

    return xx, yy


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    print("testing function: calc_cummulative_dist")
    testData = np.random.random(1000)
    pltx, plty = calc_cummulative_dist(testData, steps=100)
    plt.figure(figsize=(5, 5))
    plt.plot(pltx, plty)
    plt.show()
