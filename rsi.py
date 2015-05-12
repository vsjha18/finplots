"""
    This module plots Relative Strength Index on a given
    axis of matplotlib. All the style attributes are passed
    through argument so that it can be independently used
    as general purpose library in most of the trivial situations.

    However for ease of use we have one more sugar api which needs
    only the style object axis and the dataframe. This api simply
    calls the underlying _plot_rsi by resolving its arguments from
    the style object.
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker

from finfunctions import relative_strength_index

from finplots import style

def plot_rsi(ax, df, period=14, style=style):
    """ plot rsi
    :param ax: axis
    :param df: price dataframe
    :param style: style object
    :return: axis
    """
    rsi_data = relative_strength_index(df.close, n=period)
    legend_text = 'RSI %s' % str(period)
    ax = _plot_rsi(ax, df.index, rsi_data,
                   line_color=style.rsi_line_color,
                   line_width=style.rsi_linewidth,
                   signal_line_color=style.rsi_signal_line_color,
                   signal_line_alpha=style.rsi_signal_line_alpha,
                   fill_alpha=style.rsi_fill_alpha,
                   overbought_color=style.rsi_overbought_color,
                   oversold_color=style.rsi_oversold_color,
                   edge_color=style.rsi_edge_color,
                   label_color=style.rsi_label_color,
                   text_color=style.rsi_text_color,
                   spine_color=style.rsi_spine_color,
                   grid_alpha=style.rsi_grid_alpha,
                   grid_color=style.rsi_grid_color,
                   tick_color=style.rsi_tick_color,
                   legend_text=legend_text,
                   legend_text_x=style.legend_text_x,
                   legend_text_y=style.legend_text_y)
    # ax = _plot_rsi(ax, df.index, rsi_data)
    return ax


def _plot_rsi(ax, x, rsi_data,
              line_color='cyan',
              line_width=1,
              signal_line_color='white',
              signal_line_alpha=1,
              fill_alpha = 1,
              overbought_color='red',
              oversold_color='green',
              edge_color='cyan',
              label_color='white',
              text_color='white',
              spine_color='blue',
              grid_alpha=1,
              grid_color='white',
              tick_color='white',
              legend_text=None,
              legend_text_x=0.015,
              legend_text_y=0.95):
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
    :param tick_color: color for ticks
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
    ax.fill_between(x, rsi_data, 70,
                    where=(rsi_data >= 70),
                    facecolor=overbought_color,
                    edgecolor=edge_color,
                    alpha=fill_alpha)

    ax.fill_between(x, rsi_data, 30,
                    where=(rsi_data <= 30),
                    facecolor=oversold_color,
                    edgecolor=edge_color,
                    alpha=fill_alpha)

    # write text as legend for macd setup
    if legend_text is not None:
        ax.text(legend_text_x, legend_text_y, legend_text,
                va='top',
                color=text_color,
                transform=ax.transAxes)

    # label color
    ax.yaxis.label.set_color(label_color)

    # spine colors
    ax.spines['bottom'].set_color(spine_color)
    ax.spines['top'].set_color(spine_color)
    ax.spines['left'].set_color(spine_color)
    ax.spines['right'].set_color(spine_color)

    # tick params color
    ax.tick_params(axis='y', colors=tick_color)
    ax.tick_params(axis='x', colors=tick_color)

    # plot the grids.
    ax.grid(True, alpha=grid_alpha, color=grid_color)
    plt.ylabel('RSI', color=label_color)

    return ax
