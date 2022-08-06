from cgitb import html
from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '   <Temperature units = "c">{}</Temperature>\n'\
        .format(temperature_view(device))
    xml += '   <Pressure units = "mmHg">{}</Pressure>\n'\
        .format(pressure_view(device))
    xml += '   <Wind_Speed units = "m/s">{}</Wind_Speed>\n'\
        .format(wind_speed_view(device))
    xml += '</xml>'

    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_4/Task_1/data.xml'
    with open(path, 'w') as page:
        page.write(xml)
    
    return xml


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '   <Temperature units = "F">{}</Temperature>\n'\
        .format(t)
    xml += '   <Pressure units = "mmHg">{}</Pressure>\n'\
        .format(p)
    xml += '   <Wind_Speed units = "m/s">{}</Wind_Speed>\n'\
        .format(w)
    xml += '</xml>'

    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_4/Task_1/new_data.xml'
    with open(path, 'w') as page:
        page.write(xml)
    
    return data