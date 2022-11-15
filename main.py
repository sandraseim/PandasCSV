#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
#

#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)
#
#
import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(len(temp_list))
#
#average_temp =sum(temp_list) / (len(temp_list))
#print(average_temp)
#
#mean = data["temp"].mean()
#print(mean)
#
#max_temp = max(data["temp"])
#print(max_temp)
#
#
##Get Data in Columns
#print(data["condition"])
#print(data.condition)
#
#get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])   #finds  the row where the temp was the max
# print(data[data.temp == data.temp.min()])   #finds  the row where the temp was the min

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32  #conver temp to Farenheit
# print(monday_temp_f)


#Create a dataframe form scratch
data_dict = {
    "students": ["Amy", "James", "Jim"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
student_data.to_csv("new_data.csv")

