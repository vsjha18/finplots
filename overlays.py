"""
    module for plotting all kind of overlays on a
    candlestick chart.

"""
from finfunctions import sma, relative_strength_index
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


def plot_rsi(ax, df, style):
    """ plot rsi
    :param ax: axis
    :param df: price dataframe
    :param style: style object
    :return: axis
    """
    rsi_data = relative_strength_index(df.close, n=14)
    ax = _plot_rsi(ax, df.index, rsi_data,
                   line_color=style.rsi_line_color,
                   line_width=style.rsi_linewidth,
                   signal_line_color=style.rsi_signal_line_color,
                   signal_line_alpha=style.rsi_signal_line_alpha,
                   overbought_color=style.rsi_overbought_color,
                   oversold_color=style.rsi_oversold_color,
                   label_color=style.label_color,
                   spine_color=style.spine_color,
                   grid_alpha=style.grid_alpha,
                   grid_color=style.grid_color,
                   tick_params_color=style.tick_params_color)
    return ax


def _plot_rsi(ax, x, rsi_data,
              line_color='cyan',
              line_width=1,
              signal_line_color='white',
              signal_line_alpha=1,
              overbought_color='red',
              oversold_color='green',
              label_color='white',
              spine_color='blue',
              grid_alpha=1,
              grid_color='white',
              tick_params_color='white'):
    """ plot rsi
    :param ax: axis
    :param x: x axis series
    :param rsi_data: rsi data series
    :param line_color: rsi line color
    :param line_width: rsi line width
    :param signal_line_color: color for 30, 70 markers
    :param signal_line_alpha: alpha value for above line
    :param overbought_color: color for overbough conditions
    :param oversold_color: color for oversold conditions
    :param label_color: label color
    :param spine_color: spine color
    :param grid_alpha: alpha value for grids
    :param grid_color: color for grids
    :param tick_params_color: color for ticks
    :return: axis
    """
    ax.plot(x, rsi_data, line_color, linewidth=line_width)

    # prune the yaxis
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))

    # put markers for signal line
    # following line needs as many stuff as there are markers
    # hence we have commented this out.
    # ax2.axes.yaxis.set_ticklabels([30, 70])
    ax.set_yticks([30, 70])

    # provide the yaxis range
    ax.set_ylim(0, 100)

    # draw horizontal lines
    ax.axhline(70, color=signal_line_color, alpha=signal_line_alpha)
    ax.axhline(50, color=signal_line_color, alpha=signal_line_alpha)
    ax.axhline(30, color=signal_line_color, alpha=signal_line_alpha)

    # fill color
    ax.fill_between(x, rsi_data, 70, where=(rsi_data >= 70), facecolor=overbought_color)
    ax.fill_between(x, rsi_data, 30, where=(rsi_data <= 30), facecolor=oversold_color)
    # label color
    ax.yaxis.label.set_color(label_color)

    # spine colors
    ax.spines['bottom'].set_color(spine_color)
    ax.spines['top'].set_color(spine_color)
    ax.spines['left'].set_color(spine_color)
    ax.spines['right'].set_color(spine_color)

    # tick params color
    ax.tick_params(axis='y', colors=tick_params_color)
    ax.tick_params(axis='x', colors=tick_params_color)

    # plot the grids.
    ax.grid(True, alpha=grid_alpha, color=grid_color)
    plt.ylabel('RSI', color=label_color)

    return ax
