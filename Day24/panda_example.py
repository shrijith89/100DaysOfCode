import pandas

content = pandas.read_csv('weather_data.csv')

temperatures = content['temp'].tolist()
print(sum(temperatures) / len(temperatures))

print("The average temperature {}".format(content['temp'].mean()))
print("The maximum temperature {}".format(content['temp'].max()))
