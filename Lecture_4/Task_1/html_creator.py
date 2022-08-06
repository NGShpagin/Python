from cgitb import html
from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   <p {}>Wind_Speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   </body>\n</html>'

    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_4/Task_1/index.html'
    with open(path, 'w') as page:
        page.write(html)
    
    return html


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    style = 'style="font-size:22px"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} F</p>\n'\
        .format(style, t)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   <p {}>Wind_Speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   </body>\n</html>'

    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_4/Task_1/new_index.html'
    with open(path, 'w') as page:
        page.write(html)
    
    return data