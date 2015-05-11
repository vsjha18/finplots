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
        self.axis_bg_color = '#293035'
        self.face_color = '#293035'
        self.spine_color = '#5998ff'
        self.volume_fill_color = 'cyan'
        self.volume_line_width = 2
        self.volume_line_color = 'red'
        self.grid_color = 'white'
        self.grid_alpha = 0.2
        self.cdl_up_color = '#96E309'
        self.cdl_down_color = 'red'
        self.tick_params_color = 'white'
        self.sma_linewidth = 1.5
        self.label_color = 'white'
        self.sma_colors = ['yellow', 'blue', 'red', 'green', 'violet', 'orange', 'indigo']
        self.rsi_linewidth = 0.8
        self.rsi_line_color = 'yellow'
        self.rsi_signal_line_color = 'white'
        self.rsi_signal_line_alpha = 0.2
        self.rsi_overbought_color = self.cdl_down_color
        self.rsi_oversold_color = self.cdl_up_color