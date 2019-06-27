import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# class Transition:
#     def __init__(self, database, x_axis, y_axis):
#         self.database = database
#         self.x_axis = x_axis
#         self.y_axis = y_axis


sns.set(style="ticks")
data = pd.read_csv('countries.csv')

greece = data[data.country == 'Greece']
germany = data[data.country == 'Germany']
france = data[data.country == 'France']

df = pd.concat([greece, germany, france], axis=0)

# usable_my_data = []
# usable_outer_list = []
#
# my_data = [
#     [10.0,   8.04,   10.0,   9.14,   10.0,   7.46,   8.0,    6.58],
#     [8.0,    6.95,   8.0,    8.14,   8.0,    6.77,   8.0,    5.76],
#     [13.0,   7.58,   13.0,   8.74,   13.0,   12.74,  8.0,    7.71],
#     [9.0,    8.81,   9.0,    8.77,   9.0,    7.11,   8.0,    8.84],
#     [11.0,   8.33,   11.0,   9.26,   11.0,   7.81,   8.0,    8.47],
#     [14.0,   9.96,   14.0,   8.10,   14.0,   8.84,   8.0,    7.04],
#     [6.0,    7.24,   6.0,    6.13,   6.0,    6.08,   8.0,    5.25],
#     [4.0,    4.26,   4.0,    3.10,   4.0,    5.39,   19.0,   12.5],
#     [12.0,   10.84,  12.0,   9.13,   12.0,   8.15,   8.0,    5.56],
#     [7.0,    4.82,   7.0,    7.26,   7.0,    6.42,   8.0,    7.91],
#     [5.0,    5.68,   5.0,    4.74,   5.0,    5.73,   8.0,    6.89]]
#
# print(my_data)
#
# for outer_list in my_data:
#     if my_data.index(outer_list) == 0:
#         given_database = 'I'
#     if my_data.index(outer_list) == 1:
#         given_database = 'II'
#     if my_data.index(outer_list) == 2:
#         given_database = 'III'
#     if my_data.index(outer_list) == 3:
#         given_database = 'IV'
#     for inner_list in outer_list:
#         if outer_list.index(inner_list) // 2 == 0:
#             given_x_axis = inner_list
#         elif outer_list.index(inner_list) // 2 == 1:
#             given_y_axis = inner_list
#
#     temp_data = Transition(given_database, given_x_axis, given_y_axis)
#     usable_my_data.append(usable_outer_list)
#     for usable_outer_list in usable_my_data:
#         usable_outer_list.append(temp_data.database)
#         usable_outer_list.append(temp_data.x_axis)
#         usable_outer_list.append(temp_data.y_axis)
#
#
#
# my_data = [
#     ['I', 10.0,   8.04],
#     ['I', 8.0,    6.95],
#     ['I', 13.0,   7.58],
#     ['I', 9.0,    8.81],
#     ['I', 11.0,   8.33],
#     ['I', 14.0,   9.96],
#     ['I', 6.0,    7.24],
#     ['I', 4.0,    4.26],
#     ['I', 12.0,   10.84],
#     ['I', 7.0,    4.82],
#     ['I', 5.0,    5.68],
#     ['II', 10.0,   9.14],
#     ['II', 8.0,    8.14],
#     ['II', 13.0,   8.74],
#     ['II', 9.0,    8.77],
#     ['II', 11.0,   9.26],
#     ['II', 14.0,   8.10],
#     ['II', 6.0,    6.13],
#     ['II', 4.0,    3.10],
#     ['II', 12.0,   9.13],
#     ['II', 7.0,    7.26],
#     ['II', 5.0,    4.74],
#     ['III', 10.0,   7.46],
#     ['III', 8.0,    6.77],
#     ['III', 13.0,   12.74],
#     ['III', 9.0,    7.11],
#     ['III', 11.0,   7.81],
#     ['III', 14.0,   8.84],
#     ['III', 6.0,    6.08],
#     ['III', 4.0,    5.39],
#     ['III', 12.0,   8.15],
#     ['III', 7.0,    6.42],
#     ['III', 5.0,    5.73],
#     ['IV', 8.0,    6.58],
#     ['IV', 8.0,    5.76],
#     ['IV', 8.0,    7.71],
#     ['IV', 8.0,    8.84],
#     ['IV', 8.0,    8.47],
#     ['IV', 8.0,    7.04],
#     ['IV', 8.0,    5.25],
#     ['IV', 19.0,   12.5],
#     ['IV', 8.0,    5.56],
#     ['IV', 8.0,    7.91],
#     ['IV', 8.0,    6.89]]

df.columns = ['dataset', 'x', 'y']

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})

plt.show()
