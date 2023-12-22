import pandas as pd

weather_c = {"Monday": 12,
             "Tuesday": 14,
             "Wednesday": 15,
             "Thursday": 14,
             "Friday": 21,
             "Saturday": 22,
             "Sunday": 24}

weather_data_frame = pd.DataFrame(list(weather_c.items()), columns=['Day', 'Temperature'])
weather_data_frame = weather_data_frame.set_index('Day')

print(weather_data_frame)

for(key, value) in weather_data_frame.iterrows():
    print(key, value)
