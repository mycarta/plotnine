from .theme import theme


class theme_gray(theme):
    """
    Standard theme for ggplot. Gray background w/ white gridlines.

    Copied from the the ggplot2 codebase:
        https://github.com/hadley/ggplot2/blob/master/R/theme-defaults.r
    """
    def __init__(self):
        # super does not work well with reloads
        theme.__init__(self, complete=True)
        d = {
            'axes.axisbelow': 'True',
            'axes.edgecolor': 'bcbcbc',
            'axes.facecolor': '#E5E5E5',
            'axes.grid': 'True',
            'axes.labelcolor': 'black',
            'axes.labelsize': 'large',
            'axes.linewidth': '0',
            'axes.titlesize': 'x-large',
            'figure.edgecolor': '0.50',
            'figure.facecolor': '1.0',
            'figure.figsize': '11, 8',
            'figure.subplot.hspace': '0.5',
            'font.family': 'sans-serif',
            'font.sans-serif': ['Helvetica', 'Avant Garde',
                                'Computer Modern Sans serif', 'Arial'],
            'font.serif': ['Times', 'Palatino',
                           'New Century Schoolbook', 'Bookman',
                           'Computer Modern Roman', 'Times New Roman'],
            'font.size': '12.0',
            'grid.color': 'white',
            'grid.linestyle': 'solid',
            'grid.linewidth': '1.2',
            'legend.fancybox': 'True',
            'lines.antialiased': 'True',
            'lines.linewidth': '1.0',
            'patch.antialiased': 'True',
            'patch.edgecolor': '#E5E5E5',
            'patch.facecolor': '348ABD',
            'patch.linewidth': '0.5',
            'timezone': 'UTC',
            'xtick.color': '#7F7F7F',
            'xtick.direction': 'out',  # pointing out of axis
            'xtick.major.pad': '2',
            'xtick.major.size': '5',
            'xtick.minor.pad': '2',
            'xtick.minor.size': '0',
            'ytick.color': '#7F7F7F',
            'ytick.direction': 'out',  # pointing out of axis
            'ytick.major.pad': '0',
            'ytick.major.size': '5',
            'ytick.minor.pad': '0',
            'ytick.minor.size': '0',
        }
        self._rcParams.update(d)
