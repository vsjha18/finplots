__author__ = 'vsjha18'

"""
    This modules defines different types of candlestick charts for
     for plotting intraday and historic stock plots.
"""
# import logging
# log = logging.getLogger('finplots')
# logging.basicConfig(filename='finplots.log', filemode='w', level=logging.DEBUG)
class Style(object):
    """ class for containing all the color information """

    def __init__(self):
        # GLOBAL SETTINGS
        self.text_color = 'white'
        self.label_color = 'white'
        self.spine_color = '#5998ff'
        self.axis_bg_color = '#293035'
        self.face_color = '#293035'
        self.tick_color = 'white'
        self.grid_color = 'white'
        self.grid_alpha = 0.2
        self.edge_color = 'white'
        self.legend_text_x = 0.015
        self.legend_text_y = 0.95

        # CANDLESTICK SETTINGS
        self.volume_fill_color = 'cyan'
        self.volume_line_width = 2
        self.volume_line_color = 'red'
        self.cdl_up_color = '#96E309'
        self.cdl_down_color = 'red'

        # SMA SETTINGS
        self.sma_linewidth = 1.5
        self.sma_colors = ['orange', 'red', 'green', 'violet', 'blue', 'yellow', 'indigo']
        self.sma_alpha = 1

        # RSI SETTINGS
        self.rsi_linewidth = 0.8
        self.rsi_line_color = 'yellow'
        self.rsi_signal_line_color = 'white'
        self.rsi_signal_line_alpha = 0.2
        self.rsi_overbought_color = self.cdl_down_color
        self.rsi_oversold_color = self.cdl_up_color
        self.rsi_fill_alpha = 1
        self.rsi_text_color = self.text_color
        self.rsi_label_color = self.label_color
        self.rsi_spine_color = self.spine_color
        self.rsi_grid_color = self.grid_color
        self.rsi_grid_alpha = self.grid_alpha
        self.rsi_tick_color = self.tick_color
        self.rsi_edge_color = self.edge_color
        self.rsi_legend_text_x = self.legend_text_x
        self.rsi_legend_text_y = self.legend_text_y

        # MACD SETTINGS
        self.macd_line_color = 'blue'
        self.macd_signal_line_color = 'red'
        self.macd_div_fill_color = 'cyan'
        self.macd_div_alpha = 1
        self.macd_div_edge_color = self.edge_color
        self.macd_text_color = self.text_color
        self.macd_label_color = self.label_color
        self.macd_spine_color = self.spine_color
        self.macd_tick_color = self.tick_color
        self.macd_grid_color = self.grid_color
        self.macd_grid_alpha = self.grid_alpha
        self.macd_spine_color = self.spine_color
        self.macd_legend_text_x = self.legend_text_x
        self.macd_legend_text_y = self.legend_text_y


style = Style()