from bokeh.models import Arrow, NormalHead, Label
from bokeh.plotting import figure

DARK_RED = '#e7040f'
RED = '#ff4136'
LIGHT_RED = '#ff725c'
ORANGE = '#ff6300'
GOLD = '#ffb700'
YELLOW = '#ffde37'
LIGHT_YELLOW = '#fbf1a9'
PURPLE = '#5e2ca5'
LIGHT_PURPLE = '#a463f2'
DARK_PINK = '#d5008f'
HOT_PINK = '#ff41b4'
PINK = '#ff80cc'
LIGHT_PINK = '#ffa3d7'
DARK_GREEN = '#137752'
GREEN = '#19a974'
LIGHT_GREEN = '#9eebcf'
NAVY = '#001b44'
DARK_BLUE = '#00449e'
BLUE = '#357edd'
LIGHT_BLUE = '#96ccff'
LIGHTEST_BLUE = '#cdecff'
WASHED_BLUE = '#f6fffe'
WASHED_GREEN = '#e8fdf5'
WASHED_YELLOW = '#fffceb'
WASHED_RED = '#ffdfdf'
GREY = '#d3d3d3'
GRAY = '#d3d3d3'


def get_plot(min_x=-10, max_x=10, min_y=-10,
             max_y=10, x_color='#555555', y_color='#555555',
             hover_format='{0.[0]}'):
    TOOLTIPS = [
        ("(x,y)", "(@x, @y)")
    ]
    TOOLTIPS = ('<div style="font-family: \'Quicksand\'; font-size: 14pt; '
                'color:#555555;">'
                f'(<span style="color:{x_color};">@x{hover_format}</span>, '
                f'<span style="color:{y_color};">@y{hover_format}</span>)'
                '</div>')
    x_margin = abs(max_x - min_x) // 20
    y_margin = abs(max_y - min_y) // 20

    p = figure(x_axis_label='x-as',
               y_axis_label='y-as',
               x_range=[min_x - x_margin, max_x + x_margin],
               y_range=[min_y - y_margin, max_y + y_margin],
               tools='hover,crosshair', tooltips=TOOLTIPS)
    p.background_fill_alpha = 0
    p.border_fill_alpha = 0
    p.sizing_mode = "scale_width"
    p.tools[1].line_alpha = 0.5  # Crosshair alpha
    p.tools[1].line_width = 2  # Crosshair width

    p.xaxis[0].fixed_location = 0
    p.xaxis[0].axis_line_color = x_color
    p.xaxis[0].bounds = [min_x - x_margin / 2, max_x]
    p.xaxis[0].axis_line_cap = 'round'
    p.xaxis[0].axis_line_width = 2
    p.xaxis[0].axis_label_text_color = x_color
    p.xaxis[0].major_tick_line_color = x_color
    p.xaxis[0].major_tick_line_cap = 'round'
    p.xaxis[0].major_tick_line_width = 2
    p.xaxis[0].minor_tick_line_color = x_color
    p.xaxis[0].major_label_text_color = x_color
    p.xaxis[0].major_label_text_font_size = '14pt'
    p.xaxis[0].major_label_text_font = 'Quicksand'

    p.yaxis[0].fixed_location = 0
    p.yaxis[0].axis_line_color = y_color
    p.yaxis[0].bounds = [min_y - y_margin / 2, max_y]
    p.yaxis[0].axis_line_cap = 'round'
    p.yaxis[0].axis_line_width = 2
    p.yaxis[0].axis_label_text_color = y_color
    p.yaxis[0].major_tick_line_color = y_color
    p.yaxis[0].major_tick_line_cap = 'round'
    p.yaxis[0].major_tick_line_width = 2
    p.yaxis[0].minor_tick_line_color = y_color
    p.yaxis[0].major_label_text_color = y_color
    p.yaxis[0].major_label_text_font_size = '14pt'
    p.yaxis[0].major_label_text_font = 'Quicksand'

    p.add_layout(Arrow(end=NormalHead(size=10,
                                      line_color=y_color,
                                      fill_color=y_color,
                                      line_join='round'),
                       line_color=y_color,
                       line_width=2,
                       x_start=0, y_start=max_y,
                       x_end=0, y_end=max_y + y_margin))
    p.add_layout(Arrow(end=NormalHead(size=10,
                                      line_color=x_color,
                                      fill_color=x_color,
                                      line_join='round'),
                       line_color=x_color,
                       line_width=2,
                       x_start=max_x, y_start=0,
                       x_end=max_x + x_margin, y_end=0))

    x_label = Label(x=max_x + x_margin/10, y=.3, text='x', text_color=x_color,
                    text_font='Quicksand', text_font_size='16pt')
    y_label = Label(x=.3, y=max_y + y_margin/10, text='y', text_color=y_color,
                    text_font='Quicksand', text_font_size='16pt')
    p.add_layout(x_label)
    p.add_layout(y_label)
    p.toolbar.logo = None
    return p
