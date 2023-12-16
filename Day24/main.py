import csv

temperatures = []

with open('weather_data.csv') as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        temperature = int(row['temp'])
        temperatures.append(temperature)

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != 'temp':
            print(row[1])
