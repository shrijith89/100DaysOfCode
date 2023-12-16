import pandas

content = pandas.read_csv('weather_data.csv')

temperatures = content['temp'].tolist()
total_sum = sum(temperatures)
print(total_sum / len(temperatures))
