"""
Created on 05-Apr-2015

@author: vivejha
"""
#from . import log
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
from finplotter.overlays import plot_sma, plot_volume, plot_rsi
from finplotter import Style
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from finfunctions import relative_strength_index
from finfunctions import moving_average_convergence_divergence
from finfunctions import exponential_moving_average


# create a color scheme object
style = Style()

# global settings
#plt.style.use('dark_background')
#plt.style.use('ggplot')
# changes the fontsize
matplotlib.rcParams.update({'font.size':10})
#log.info('testing logger')
def candlestick_plot(df,
                     smas=[26, 5],
                     style=style,
                     figsize=(12,8),
                     macd_setup = dict(slow=26, fast=12, ema=9)
                     ):
    """ plot candlestick chart """

    fig = plt.figure(figsize=figsize, facecolor=style.face_color)  # 18, 10 for full screen

    # create main axis for charting prices
    ax1 = plt.subplot2grid((10,4), (0,0),
                           rowspan=8,
                           colspan=4,
                           axisbg=style.axis_bg_color)

    if 'volume' not in df:
        df['volume'] = np.zeros(len(df))
#   times = pd.date_range('2014-01-01', periods=l, freq='1d')
    df.date = pd.to_datetime(df.date)
    df.date = [mdates.date2num(d) for d in df.date]

    df = df[::-1]
    payload = df[['date', 'open', 'high', 'low', 'close', 'volume']].values
    candlestick_ohlc(ax1, payload, width=0.5, colorup=style.cdl_up_color, colordown=style.cdl_down_color)

    annotate_max(ax1, df)

    ax1.grid(True, alpha=style.grid_alpha, color=style.grid_color)
    plt.ylabel('Stock Price', color=style.label_color)

    # determines number of points to be displayed on x axis
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(50))

    # determines format of markers on the xaxis
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))

    # label color
    ax1.yaxis.label.set_color(style.label_color)

    # tick params color
    ax1.tick_params(axis='y', colors=style.tick_params_color)


    # spine colors
    ax1.spines['bottom'].set_color(style.spine_color)
    ax1.spines['top'].set_color(style.spine_color)
    ax1.spines['left'].set_color(style.spine_color)
    ax1.spines['right'].set_color(style.spine_color)

    # make the x tick label invisible
    plt.setp(ax1.get_xticklabels(), visible=False)

    # plot all the simple moving averages
    for idx, period in enumerate(smas):
        ax1 = plot_sma(df, ax1,
                 period=period,
                 color=style.sma_colors[idx],
                 linewidth=style.sma_linewidth)

    # display the legend
    plt.legend(loc=0, fancybox=True)

    # co-plot the volume data on the same axis
    if 'volume' in df:
        plot_volume(df, ax1,
                    fill_color=style.volume_fill_color,
                    spine_color=style.spine_color,
                    color=style.volume_line_color,
                    linewidth=style.volume_line_width,
                    tick_color=style.tick_params_color)

    ######################################
    ##            RSI Code              ##
    ######################################
    ax_rsi = plt.subplot2grid((10,4), (9,0),
                           rowspan=1,
                           colspan=4,
                           sharex=ax1,
                           axisbg=style.axis_bg_color)
    rsi_data = relative_strength_index(df.close)
    from finplotter.overlays import _plot_rsi
    plot_rsi(ax_rsi, df, style)

    ################################
    ##          MACD Code         ##
    ################################
    ax3 = plt.subplot2grid((10,4), (8,0),
                           rowspan=1,
                           colspan=4,
                           sharex=ax1,
                           axisbg=style.axis_bg_color)

    nslow = macd_setup['slow']
    nfast = macd_setup['fast']
    nema = macd_setup['ema']

    ema_fast, ema_slow, macd = moving_average_convergence_divergence(df.close)
    ema9 = exponential_moving_average(macd, nema)

    ax3.plot(df.index, macd, linewidth=2, color='lime')
    ax3.plot(df.index, ema9, linewidth=2, color='hotpink')




    # FROM HERE
    # prune the yaxis
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='lower'))

    # print text
    ax3.text(0.015, 0.95, 'MACD 12,26,9', va='top', color='white', transform=ax3.transAxes)
    # put markers for signal line
    # following line needs as many stuff as there are markers
    # hence we have commented this out.
    # ax_rsi.axes.yaxis.set_ticklabels([30, 70])

    #ax3.set_yticks([])

    # provide the yaxis range
    #ax3.set_ylim(0, 100)

    # draw horizontal lines
    # ax3.axhline(70, color=style.rsi_signal_line_color, alpha=style.rsi_signal_line_alpha)
    # ax3.axhline(50, color=style.rsi_signal_line_color, alpha=style.rsi_signal_line_alpha)
    #ax3.axhline(0, color='w')
    # ax3.axhline(30, color=style.rsi_signal_line_color, alpha=style.rsi_signal_line_alpha)

    # fill color
    div = macd - ema9
    ax3.fill_between(df.index, div, 0, facecolor='deepskyblue', edgecolor='w', alpha=0.3)

    # ax3.fill_between(df.index, rsi_data, 30, where=(rsi_data<=30), facecolor=style.rsi_oversold_color)
    # label color
    ax3.yaxis.label.set_color(style.label_color)

    # spine colors
    ax3.spines['bottom'].set_color(style.spine_color)
    ax3.spines['top'].set_color(style.spine_color)
    ax3.spines['left'].set_color(style.spine_color)
    ax3.spines['right'].set_color(style.spine_color)

    # tick params color
    ax3.tick_params(axis='y', colors='w')
    ax3.tick_params(axis='x', colors='w')

    # plot the grids.
    ax3.grid(True, alpha=style.grid_alpha, color=style.grid_color)
    plt.ylabel('MACD', color=style.label_color)
    plt.setp(ax3.get_xticklabels(), visible=False)
    # Till here




    # make the labels a bit rotated for better visibility
    for label in ax_rsi.xaxis.get_ticklabels():
        label.set_rotation(45)

    # adjust the size of the plot
    #plt.subplots_adjust(left=0.10, bottom=0.19, right=0.93, top=0.95, wspace=0.20, hspace=0.0)
    plt.subplots_adjust(left=0.07, bottom=0.10, right=0.97, top=0.95, wspace=0.20, hspace=0.0)

    plt.xlabel('Date', color=style.label_color)
    plt.suptitle('Stock Price Chart', color=style.label_color)

    plt.show()


def annotate_max(ax, df, text='Max'):
    #import ipdb; ipdb.set_trace()
    max = df.high.max()
    idx = df.high.tolist().index(max)
    ax.annotate(text,
                xy=(df.date[idx], df['high'][idx]),  # theta, radius
                xytext=(0.5, 1),    # fraction, fraction
                xycoords='data',
                textcoords='axes fraction',
                arrowprops=dict(facecolor='grey', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='bottom',
                )

def marker(idx, ycord, text, orgin, color):
    pass

