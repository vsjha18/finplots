import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker

from finfunctions import moving_average_convergence_divergence
from finfunctions import exponential_moving_average

from finplots import style

def plot_macd(ax, df, style=style, slow=26, fast=12, ema=9):
    """ plot macd given axis and dataframe
    :param ax: matplotlib axis
    :param df: dataframe object containing prices
    :param style: style
    :return: axis
    """
    ema_fast, ema_slow, macd = moving_average_convergence_divergence(df.close)
    ema9 = exponential_moving_average(macd, ema)
    legend_text = 'MACD %s, %s, %s' % (str(slow), str(fast), str(ema))
    ax = _plot_macd(ax, df.index, macd, ema9,
                    macd_line_color=style.macd_line_color,
                    macd_line_width=style.macd_line_width,
                    signal_line_color=style.macd_signal_line_color,
                    signal_line_width=style.macd_signal_line_width,
                    fill_color=style.macd_div_fill_color,
                    edge_color=style.macd_div_edge_color,
                    div_alpha=style.macd_div_alpha,
                    label_color=style.macd_label_color,
                    spine_color=style.macd_spine_color,
                    tick_color=style.macd_tick_color,
                    text_color=style.macd_text_color,
                    grid_color=style.macd_grid_color,
                    grid_alpha=style.macd_grid_alpha,
                    legend_text = legend_text,
                    legend_text_x=style.macd_legend_text_x,
                    legend_text_y=style.legend_text_y
                    )
    # ax = _plot_macd(ax, df.index, macd, ema9)
    return ax

def _plot_macd(ax, x, macd, ema,
               macd_line_color='yellow',
               macd_line_width=1.5,
               signal_line_color='lime',
               signal_line_width=1.5,
               fill_color='cyan',
               edge_color='white',
               div_alpha=0.5,
               label_color='white',
               spine_color='blue',
               tick_color='white',
               text_color='white',
               grid_color='white',
               grid_alpha=0.5,
               legend_text=None,
               legend_text_x=0.015,
               legend_text_y=0.95
               ):

    # plot_macd(ax_macd, df, style=style, slow=macd_setup['slow'], fast=macd_setup['fast'], ema=macd_setup['nema'] )
    ax.plot(x, macd, linewidth=macd_line_width, color=macd_line_color)
    ax.plot(x, ema, linewidth=signal_line_width, color=signal_line_color)


    ax.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='lower'))

    # write text as legend for macd setup
    if legend_text is not None:
        ax.text(legend_text_x, legend_text_y, legend_text,
                va='top',
                color=text_color,
                transform=ax.transAxes)

    # plot macd divergence
    div = macd - ema
    ax.fill_between(x, div, 0, facecolor=fill_color, edgecolor=edge_color, alpha=div_alpha)

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
    plt.ylabel('MACD', color=label_color)
    plt.setp(ax.get_xticklabels(), visible=False)
    return ax

