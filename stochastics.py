import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker

from finfunctions import slow_stochastic

from finplots import style


def plot_slow_stochastic(ax, df, period=14, smoothing=3):
    """ plot slow stochastic
    :param ax:
    :param df:
    :param period:
    :param smoothing:
    :return:
    """
    k, d = slow_stochastic(df.low, df.high, df.close, period=14, smoothing=3)
    legend_text = 'SLOW STOCH %s, %s' % (str(period), str(smoothing))
    ax = _plot_slow_stochastic(ax, df.index, k, d,
                               k_line_color=style.sstoch_k_line_color,
                               k_line_width=style.sstoch_k_line_width,
                               d_line_color=style.sstoch_d_line_color,
                               d_line_width=style.sstoch_d_line_width,
                               text_color=style.sstoch_text_color,
                               label_color=style.sstoch_label_color,
                               spine_color=style.sstoch_spine_color,
                               tick_color=style.sstoch_tick_color,
                               grid_color=style.sstoch_grid_color,
                               grid_alpha=style.sstoch_grid_alpha,
                               legend_text_x=style.sstoch_legend_text_x,
                               legend_text_y=style.sstoch_legend_text_y,
                               hline_color=style.sstoch_hline_color,
                               hline_width=style.sstoch_hline_width,
                               hline_alpha=style.sstoch_hline_alpha,
                               legend_text=legend_text)
    return ax


def _plot_slow_stochastic(ax, x, k, d,
                          k_line_color='orange',
                          k_line_width=1,
                          d_line_color='cyan',
                          d_line_width=1,
                          text_color='white',
                          label_color='white',
                          spine_color='blue',
                          tick_color='white',
                          grid_color='white',
                          grid_alpha=1,
                          legend_text_x=0.015,
                          legend_text_y=0.95,
                          hline_color='white',
                          hline_width=1,
                          hline_alpha=1,
                          legend_text=None):
    """ plot slow stochastic
    :param ax:
    :param x:
    :param k:
    :param d:
    :param k_line_color:
    :param k_line_width:
    :param d_line_color:
    :param d_line_width:
    :param text_color:
    :param label_color:
    :param spine_color:
    :param tick_color:
    :param grid_color:
    :param grid_alpha:
    :param legend_text_x:
    :param legend_text_y:
    :return:
    """

    ax.plot(x[-len(k):], k, linewidth=k_line_width, color=k_line_color)
    ax.plot(x[-len(d):], d, linewidth=d_line_width, color=d_line_color)

    # prune the y axis
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))

    # put markers for signal line
    # following line needs as many stuff as there are markers
    # hence we have commented this out.
    # ax2.axes.yaxis.set_ticklabels([30, 70])
    ax.set_yticks([20, 80])

    # provide the y axis range
    ax.set_ylim(0, 100)

    # draw horizontal lines
    ax.axhline(80, color=hline_color, alpha=hline_alpha, linewidth=hline_width)
    ax.axhline(50, color=hline_color, alpha=hline_alpha, linewidth=hline_width)
    ax.axhline(20, color=hline_color, alpha=hline_alpha, linewidth=hline_width)

    # # fill color
    # ax.fill_between(x, rsi_data, 70,
    #                 where=(rsi_data >= 70),
    #                 facecolor=overbought_color,
    #                 edgecolor=edge_color,
    #                 alpha=fill_alpha)
    #
    # ax.fill_between(x, rsi_data, 30,
    #                 where=(rsi_data <= 30),
    #                 facecolor=oversold_color,
    #                 edgecolor=edge_color,
    #                 alpha=fill_alpha)

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
    plt.ylabel('S STOCH', color=label_color)
    plt.setp(ax.get_xticklabels(), visible=False)

    return ax
