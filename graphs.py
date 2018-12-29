from bokeh.models import Arrow, NormalHead, ColumnDataSource
from bokeh.models.glyphs import Text
from bokeh.plotting import figure


def get_plot(min_x=-10, max_x=10, min_y=-10,
             max_y=10, x_color='#555555', y_color='#555555'):
    TOOLTIPS = [
        ("(x,y)", "(@x, @y)")
    ]
    TOOLTIPS =  ('<div style="font-family: \'Quicksand\'; font-size: 14pt; color:#555555;">'
                 f'(<span style="color:{x_color};">@x{{0.[0]}}</span>, '
                 f'<span style="color:{y_color};">@y{{0.[0]}}</span>)'
                 '</div>')
    x_margin = abs(max_x - min_x) // 20
    y_margin = abs(max_y - min_y) // 20

    p = figure(x_axis_label='x-as',
               y_axis_label='y-as',
               x_range=[min_x - x_margin, max_x + x_margin],
               y_range=[min_y - y_margin, max_y + y_margin],
               tools='hover, crosshair', tooltips=TOOLTIPS)
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

    source = ColumnDataSource(dict(x=[max_x + 0.3, .4],
                                   y=[.4, max_y + 0.3],
                                   text=['x', 'y'],
                                   text_color=[x_color, y_color]))
    glyph = Text(x='x', y='y', text='text', text_color='text_color', text_font='Quicksand', text_font_size='16pt')
    p.add_glyph(source, glyph)
    p.toolbar.logo = None
    return p
