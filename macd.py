import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker

from finfunctions import moving_average_convergence_divergence
from finfunctions import exponential_moving_average

def plot_macd(ax, df, style, slow=26, fast=12, ema=9):
    """ plot macd given axis and dataframe
    :param ax: matplotlib axis
    :param df: dataframe object containing prices
    :param style: style
    :return: axis
    """
    ema_fast, ema_slow, macd = moving_average_convergence_divergence(df.close)
    ema9 = exponential_moving_average(macd, ema)
    ax = _plot_macd(ax, df.index, macd, ema9,
                    macd_line_color=style.macd_line_color,
                    signal_line_color=style.macd_signal_line_color,
                    fill_color=style.macd_div_fill_color,
                    edge_color=style.macd_div_edge_color,
                    div_alpha=style.macd_div_alpha,
                    label_color=style.macd_label_color,
                    spine_color=style.macd_spine_color,
                    tick_color=style.macd_tick_color,
                    text_color=style.macd_text_color,
                    grid_color=style.macd_grid_color,
                    grid_alpha=style.macd_grid_alpha
                    )

def _plot_macd(ax, x, macd, ema9,
               macd_line_color='yellow',
               signal_line_color='lime',
               fill_color='cyan',
               edge_color='white',
               div_alpha=0.5,
               label_color='white',
               spine_color='blue',
               tick_color='white',
               text_color='white',
               grid_color='white',
               grid_alpha=0.5
               ):

    # plot_macd(ax_macd, df, style=style, slow=macd_setup['slow'], fast=macd_setup['fast'], ema=macd_setup['nema'] )
    ax.plot(x, macd, linewidth=2, color=macd_line_color)
    ax.plot(x, ema9, linewidth=2, color=signal_line_color)


    ax.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='lower'))

    # write text as legend for macd setup
    ax.text(0.015, 0.95, 'MACD 12,26,9', va='top', color=text_color, transform=ax.transAxes)

    # plot macd divergence
    div = macd - ema9
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

