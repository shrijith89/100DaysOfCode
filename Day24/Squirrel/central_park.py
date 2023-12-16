import pandas
gray_count = 0

content = pandas.read_csv('Central_Park_Squirrel_Census.csv')

gray_color = content['Primary Fur Color'] == 'Gray'
red_color = content['Primary Fur Color'] == 'Red'
black_color = content['Primary Fur Color'] == 'Black'


data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_color.count(), red_color.count(), black_color.count()]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
