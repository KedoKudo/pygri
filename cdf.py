#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pygri.pltmath import calc_cummulative_dist


def cdf(data, 
        labels=None, labelsize='small', 
        figureSize=(3,3), 
        cmap="Blues", steps=100,
        xlim=None, ylim=None,
        xscale="linear", yscale="linear",
        ):
    """
    description:
        Generate cumulative distribution plot(s) that similar with a style
        similar to GRI plot
    args:
        data:       numpy array | pandas DataFrame
            Data for plotting
        labels:     strs | list of strs
            Labels for each set of data. If DataFrame is passed, it is also
            used to quert the data column from given DataFrame.
        labelsize:  label size contorl 
            Valid input inlcudes: 
            large, medium, smaller, small, x-large, xx-small, 
            larger, x-small, xx-large, None
        figureSize: tuple
            Figure size in inches.
        cmap:       Matplotlib built-in cmap names
            If multiple data are passed, this cmap is used to map the variation 
            among given datas.
        steps:      Int
            Number of data points plotted on figure.
        x/yscale:   specify axis types
            valid options = [“linear”, “log”, “symlog”, “logit”]
    returns:
        fig:        Matplotlib figure instance 
            A figure instance is returned for futher tweaking if necessary
        ax:         Matplotlib axes handle
            Allow further tweaking outside the function
    """
    # figure out data size if not enough information is given
    if isinstance(data, pd.DataFrame):
        labels = data.columns if labels is None else labels
        pltdata = data[labels].as_matrix()
    else:
        pltdata = data
        try:
            column_nums = data.shape[1]
        except:
            column_nums = 1
        labels = ["data_{}".format(i+1) for i in xrange(column_nums)]
    
    # setting up figure
    fig = plt.figure(figsize=figureSize, dpi=300)
    ax = fig.add_subplot(1, 1, 1)

    # prepare color for each data array
    if len(labels) > 1:
        cmap = plt.get_cmap(cmap)
        clrs = cmap(np.linspace(0.1, 0.9, len(labels)))
    
    for i, label in enumerate(labels):
        _pltx, _plty = calc_cummulative_dist(pltdata[:, i], steps=steps)
        ax.plot(_pltx, _plty, color=clrs[i], label=label)
    
    # formatting ticks to mimic GRI output
    ax.tick_params(direction='in', 
                   length=3, width=0.2,
                   labelsize=labelsize, pad=1,
                   which='both',
                   bottom='on', left='on', right='on', top='on',
                   )
    ax.minorticks_on()
    ax.locator_params(tight=True, nbins=4)
    ax.set_xscale(xscale), ax.set_yscale(yscale)

    # set axis limits if specified
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    return fig, ax

if __name__ == "__main__":
    testData = np.random.random((1000, 3))
    testData[:, 1] += 0.5
    testData[:, 2] -= 0.5
    df = pd.DataFrame(testData)
    df.columns = ['a', 'b', 'c']
    fig, ax = cdf(df, labels=df.columns, cmap='Reds',
                  figureSize=(1,1), labelsize=3,
                  xlim=(-0.5, 1.5), ylim=(0.0, 1.0),
                  )
    plt.show()
