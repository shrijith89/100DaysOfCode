import pandas

content = pandas.read_csv('weather_data.csv')

temperatures = content['temp'].tolist()
print(sum(temperatures) / len(temperatures))

print("The average temperature {}".format(content['temp'].mean()))
print("The maximum temperature {}".format(content['temp'].max()))
print("Details of {}".format(content[content.temp == content.temp.max()]))

#Create a dataframe

data_dict = {
    "students": ["ram", "shyam", "bheem"],
    "scores": [67, 74, 77]
}

data = pandas.DataFrame(data_dict)
data.to_csv("mydataframe.csv")
