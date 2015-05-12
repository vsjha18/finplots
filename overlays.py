"""
    module for plotting all kind of overlays on a
    candlestick chart.

"""
from finfunctions import sma
from finfunctions import relative_strength_index
from finfunctions import moving_average_convergence_divergence
from finfunctions import exponential_moving_average

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plot_sma(df, ax, color='cyan', linewidth=1, period=26, label=None, alpha=1):
    """
    create simple moving average overlay

    :param df: dataframe object containing stock data
    :param ax: axis on which the plot is required.
    :param period: period for sma
    :param style: color scheme object
    :return: axis
    """
    if label is None:
        label = str(period) + ' SMA'
    ma = sma(df['close'], period)
    ax.plot(df.date[-len(ma):], ma, color, label=label, linewidth=linewidth, alpha=alpha)
    return ax


def plot_volume(df, ax, spine_color='blue', fill_color=None, linewidth=1, color='yellow', tick_color='white'):
    """ overlay volume data on the given axis
    :param df: pandas dataframe containing OHLC data
    :param ax: axis on which it has to be overlayed.
    :return: axis
    """
    axv = ax.twinx()
    axv.fill_between(df.date, df.volume,
                     facecolor=fill_color,
                     alpha=0.5,
                     linewidth=linewidth,
                     color=color)

    # remove all the tick labels on the y-axis
    axv.axes.yaxis.set_ticklabels([])

    # set spine color, because it gets reset due to twinx
    axv.spines['bottom'].set_color(spine_color)
    axv.spines['top'].set_color(spine_color)
    axv.spines['left'].set_color(spine_color)
    axv.spines['right'].set_color(spine_color)

    # limit the height pf the plot
    axv.set_ylim(0, 8 * df.volume.max())
    # axv.tick_params(axis='x', colors=style.tick_params_color)

    # set tick colors because it gets reset due to twinx
    axv.tick_params(axis='y', colors=tick_color)
    return ax


