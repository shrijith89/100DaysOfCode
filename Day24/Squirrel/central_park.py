import pandas

content = pandas.read_csv('Central_Park_Squirrel_Census.csv')

gray_count = (content['Primary Fur Color'] == 'Gray').count()
red_count = (content['Primary Fur Color'] == 'Red').count()
black_count = (content['Primary Fur Color'] == 'Black').count()


data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
