"""
    This module is for plotting all kinds of overlays,
    for example SMA, Volume, Bollinger Bands etc. Overlays
    are plots which doesn't needs a separate axis for being
    plotted. They are co-plotted on an existing axis just to
    make the more insight to the main data.
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from finfunctions import simple_moving_average
from finfunctions import bollinger_bands

from finplots import style


def plot_sma(ax, df, period, color='cyan', style=style):
    sma = simple_moving_average(df.close, period=period)
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


def plot_volume(ax, df, style=style):
    ax = _plot_volume(ax, df.index, df.volume,
                      spine_color=style.spine_color,
                      fill_color=style.volume_fill_color,
                      fill_alpha=style.volume_fill_alpha,
                      edge_color=style.volume_edge_color,
                      line_width=style.volume_line_width,
                      color=style.volume_line_color,
                      tick_color=style.tick_color)
    return ax

def _plot_volume(ax, x, volume,
                spine_color='blue',
                fill_color=None,
                fill_alpha=0.5,
                edge_color='yellow',
                line_width=1,
                color='yellow',
                tick_color='white'):
    """ overlay volume data on the given axis
    :param df: pandas dataframe containing OHLC data
    :param ax: axis on which it has to be overlayed.
    :return: axis
    """
    axv = ax.twinx()
    axv.fill_between(x, volume,
                     facecolor=fill_color,
                     alpha=fill_alpha,
                     linewidth=line_width,
                     color=color,
                     edgecolor=edge_color)

    # remove all the tick labels on the y-axis
    axv.axes.yaxis.set_ticklabels([])

    # set spine color, because it gets reset due to twinx
    axv.spines['bottom'].set_color(spine_color)
    axv.spines['top'].set_color(spine_color)
    axv.spines['left'].set_color(spine_color)
    axv.spines['right'].set_color(spine_color)

    # limit the height pf the plot
    axv.set_ylim(0, 8 * volume.max())
    # axv.tick_params(axis='x', colors=style.tick_params_color)

    # set tick colors because it gets reset due to twinx
    axv.tick_params(axis='y', colors=tick_color)
    return ax


def plot_bollinger_bands(ax, df, period=20):
    """ plot bollinger bands
    :param ax: mpl axis on which to plot
    :param df: dataframe object
    :param period: period for calculating bollinger bands
    :return: axis
    """
    lower, middle, upper = bollinger_bands(df.close, period=period)
    ax = _plot_bollinger_bands(ax, df.index, lower, middle, upper,
                               mid_line_color=style.bbands_mid_line_color,
                               mid_line_width=style.bbands_mid_line_width,
                               fill_color=style.bbands_fill_color,
                               fill_alpha=style.bbands_fill_alpha,
                               edge_color=style.bbands_edge_color,
                               edge_line_width=style.bbands_edge_line_width,
                               text_color=style.bbands_text_color)

    #ax = _plot_bollinger_bands(ax, df.index, lower, middle, upper)
    return ax

def _plot_bollinger_bands(ax, x, lower, middle, upper,
                          mid_line_color='red',
                          mid_line_width=1,
                          fill_color='cyan',
                          fill_alpha=0.5,
                          edge_color='cyan',
                          edge_line_width=1,
                          text_color='white'):
    """
    :param ax: mpl axis on which it has to be plotted
    :param prices: prices for which
    :param period:
    :param mid_line_color:
    :param mid_line_width:
    :param fill_color:
    :param fill_alpha:
    :param edge_color:
    :param edge_line_width:
    :param text_color:
    :return:
    """
    ax.plot(x[-len(middle):], middle, color=mid_line_color, linewidth=mid_line_width)
    ax.fill_between(x[-len(middle):], upper, lower,
                    color=fill_color,
                    alpha=fill_alpha,
                    linewidth=edge_line_width,
                    edgecolor=edge_color)
    return ax



