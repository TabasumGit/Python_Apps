import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))
    # print(data)
city  = input('enter a city')

for row in data[1:]:
    
    # print(row)
    if row[0] == city:
        print(row[0])