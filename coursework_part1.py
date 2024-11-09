# importing necessary packages
import csv
import math
import matplotlib.pyplot as plt


# defining NDVI formula
def ndvi(r_nir, r_red):
    return (r_nir - r_red) / (r_nir + r_red)


# accessing and creating a list of the NIR light intensities
with open('band_NIR.csv', 'r') as file:
    reader = csv.reader(file)
    nir_data = list(reader)

# accessing and creating a list of the red light intensities
with open('band_red.csv', 'r') as file:
    reader2 = csv.reader(file)
    red_data = list(reader2)

# creation of empty lists for data storage
ndvi_array = []
nir_row = []
red_row = []
ndvi_row = []
# for loop indexes each row of data from both nir and red csv files
for n in range(1, 2313):
    # for loop that accesses each element in a given row
    for e in range(1, 4377):
        nir_row.append(float(nir_data[n][e]))  # temporary row of nir data created
        red_row.append(float(red_data[n][e]))  # temporary row of red data created#
        calc = float(ndvi(nir_row[-1], red_row[-1]))  # last element in each temporary list is inputted into formula
        ndvi_row.append(round(calc, 3))  # each calculation added to empty list to create row of processed data
    ndvi_array.append(ndvi_row)  # add row of ndvi calculations to new matrix/list of lists
    # all temporary lists are cleared for next row of data to be processes
    nir_row = []
    red_row = []
    ndvi_row = []

print('A 5x5 array of the complete 4377x2312 NDVI array: ')
print()
# loop that prints and arranges the first 5 rows and columns of the calculated NDVI array
for i in range(5):
    for j in range(5):
        print(ndvi_array[i][j], end='\t')
    print()

# empty line to separate the following print
print()

list_range1 = []  # list of elements where NDVI < 0
list_range2 = []  # list of elements where 0 ≤ NDVI < 0.3
list_range3 = []  # list of elements where 0.3 ≤ NDVI < 0.6
list_range4 = []  # list of elements where 0.6 ≤ NDVI < 0.9
list_range5 = []  # list of elements where NDVI ≥ 0.9

# sorting each NDVI element into its category
for v in range(len(ndvi_array)):  # for loop accesses each row in row
    for p in range(len(ndvi_array[0])):  # for loop accesses each element in given row
        if float(ndvi_array[v][p]) < 0:
            list_range1.append(ndvi_array[v][p])
        elif float(ndvi_array[v][p]) < 0.3:
            list_range2.append(ndvi_array[v][p])
        elif float(ndvi_array[v][p]) < 0.6:
            list_range3.append(ndvi_array[v][p])
        elif float(ndvi_array[v][p]) < 0.9:
            list_range4.append(ndvi_array[v][p])
        else:
            list_range5.append(ndvi_array[v][p])

# printing the results
print('The number of array elements in category:')
print()
print('NDVI < 0 : ', len(list_range1))
print('0 ≤ NDVI < 0.3 : ', len(list_range2))
print('0.3 ≤ NDVI < 0.6 : ', len(list_range3))
print('0.6 ≤ NDVI < 0.9 : ', len(list_range4))
print('NDVI ≥ 0.9 : ', len(list_range5))
print()


# defining equation for predicted NDVI values
def ndviP(SWP):
    return (0.26 * SWP) + 0.96


# lists of SWP values for 2019
swp2019 = [-2.196, -2.511, -2.261, -3.964, -3.078]

# creating empty list for predicted NDVI values
ndviP2019 = []

# for loop calculates predicted NDVI values from 2019 SWP values and adds them to their list
for v in range(len(swp2019)):
    ndviP_value = round(ndviP(swp2019[v]), 3)
    ndviP2019.append(ndviP_value)

# printing results
print('Predicted NDVI values calculated from 2019 SWP values: ')
print()
print('Element (605, 1100) = ', ndviP2019[0])
print('Element (3712, 500) = ', ndviP2019[1])
print('Element (2124, 1072) = ', ndviP2019[2])
print('Element (196, 85) = ', ndviP2019[3])
print('Element (4100, 2241) = ', ndviP2019[4])
print()

# list of measured NDVI values for comparing with predicted NDVI values.
# question is unclear on which exact elements required, and can change ...
# depending on how you interpret what they're telling you to index ...
# this indexing was based on TA advice
ndviM = [ndvi_array[1100][650], ndvi_array[500][3712],
         ndvi_array[1072][2124], ndvi_array[85][196],
         ndvi_array[2241][4100]]


# defining RMSE equation
def rmse(N, total_sum):
    return round(math.sqrt((1 / N) * total_sum), 3)


# defining the main function within the RMSE equation
def sum_function(ym, yp):
    return (ym - yp) ** 2


# for loop loops through both sets to calculate RMSE between measured and predicted data
for f in range(len(ndviM)):
    summation = 0
    summation += sum_function(ndviM[f], ndviP2019[f])
numb_N = int(len(ndviM))
rmse_result = rmse(numb_N, summation)
print('The RMSE between the measured NDVI values and the predicted NDVI values = ', rmse_result)

# creating lists for the rest of the years of SWP data
swp2020 = [-1.974, -2.169, -2.154, -3.399, -2.473]
swp2021 = [-1.82, -2.01, -1.929, -2.745, -2.423]
swp2022 = [-1.772, -1.63, -1.649, -2.648, -2.129]

# empty lists to put predicted NDVI values into
ndviP2020 = []
ndviP2021 = []
ndviP2022 = []

# repeating the process done earlier where predicted NDVI are generated from SWP values,
# this time for all the other years
for b in range(len(swp2020)):
    ndviP_value = round(ndviP(swp2020[b]), 3)
    ndviP2020.append(ndviP_value)
    ndviP_value = round(ndviP(swp2021[b]), 3)
    ndviP2021.append(ndviP_value)
    ndviP_value = round(ndviP(swp2022[b]), 3)
    ndviP2022.append(ndviP_value)

# list of years
years = [2019, 2020, 2021, 2022]

# location 1 = element(605, 1100)
# location 2 = element(3712, 500)
# location 3 = element(2124, 1072)
# location 4 = element(196, 85)
# location 5 = element(4100, 2241)

# dictionary with each key being the location and the values being ...
# the list of predicted NDVI values
location_dict = {}
for i in range(5):
    num = str(i + 1)
    key = 'location' + num
    list_values = [ndviP2019[i], ndviP2020[i], ndviP2021[i], ndviP2022[i]]
    location_dict[key] = list_values

# plotting the data
plt.figure()
plt.plot(years, location_dict['location1'], label="location 1 - element(605, 1100)")
plt.plot(years, location_dict['location2'], label="location 2 - element(3712, 500)")
plt.plot(years, location_dict['location3'], label="location 3 - element(2124, 1072)")
plt.plot(years, location_dict['location4'], label="location 4 - element(196, 85)")
plt.plot(years, location_dict['location5'], label="location 5 - element(4100, 2241)")
plt.xlabel('Year')
plt.ylabel('Predicted NDVI values')
plt.legend()

# saves the image as specified
plt.savefig('ex1_question5.png')
