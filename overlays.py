"""
    This module is for plotting all kinds of overlays,
    for example SMA, Volume, Bollinger Bands etc. Overlays
    are plots which doesn't needs a separate axis for being
    plotted. They are co-plotted on an existing axis just to
    make the more insight to the main data.
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from finfunctions import simple_moving_aveage
from finplots import style

def plot_sma(ax, df, period, color='cyan', style=style):
    sma = simple_moving_aveage(df.close, period=period)
    legend_text = '%s SMA' % str(period)
    ax = _plot_sma(ax, df.index, sma,
                   color=color,
                   line_width=style.sma_linewidth,
                   alpha=style.sma_alpha,
                   legend_text=legend_text)
    return ax

def _plot_sma(ax, x, sma,
              color='cyan',
              line_width=1,
              legend_text=None,
              alpha=1):
    """
    create simple moving average overlay

    :param df: dataframe object containing stock data
    :param ax: axis on which the plot is required.
    :param period: period for sma
    :param style: color scheme object
    :return: axis
    """
    ax.plot(x[-len(sma):], sma, color, label=legend_text, linewidth=line_width, alpha=alpha)
    if legend_text is not None:
        plt.legend(loc=0, fancybox=True)
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


