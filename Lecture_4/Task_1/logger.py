from datetime import datetime as dt

log_path = '/Users/nikolaishpagin/Desktop/GeekBrains/Программист (1 четверть)/Знакомство с Python/Lecture_4/Task_1/log.csv'

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(log_path, 'a') as file:
        file.write('{} Temperature: {}\n'.format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(log_path, 'a') as file:
        file.write('{} Pressure: {}\n'.format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(log_path, 'a') as file:
        file.write('{} Wind_speed: {}\n\n'.format(time, data))
