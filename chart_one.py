import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv

sns.set(style="darkgrid")

####
# i am loading the data from the excel file, choosing the 3 countries and forming it to match the dataframe that
# FacetGrid accepts
####

data = pd.read_csv('countries.csv')
greece = data[data.country == 'Greece']
germany = data[data.country == 'Germany']
france = data[data.country == 'France']
df = pd.concat([greece, germany, france], axis=0)
temp_data = {'year': df.year, 'population': df.population, 'country': df.country}
new_data = pd.DataFrame(temp_data)

####
# at this point i am trying to to find the top/bot values through the year-section in order to set the limit of the x
# axis and he top value through the population-section in order to set the y axis
####

set_axes = new_data.year.tolist()
set_y_lim = new_data.population.tolist()
top_number = set_axes[0]
bot_number = set_axes[0]

for num in set_axes:
    if num < bot_number:
        bot_number = num

for num in set_axes:
    if num > top_number:
        top_number = num

bins = np.linspace(bot_number, top_number)

top_number_y = set_y_lim[0]
for num in set_y_lim:
    if num > top_number_y:
        top_number_y = num

g = sns.FacetGrid(new_data, col="country", sharey='all', margin_titles=True, ylim=(0, top_number_y), xlim=(bot_number, top_number))
g.map(plt.hist, 'year', color="steelblue", bins=bins)

plt.show()
