import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

#########################################
# Opening the excel and extracting data #
#########################################

data = pd.read_csv('countries.csv')
greece = data[data.country == 'Greece']
germany = data[data.country == 'Germany']
france = data[data.country == 'France']

#############
# Chart One #
#############

df = pd.concat([greece, germany, france], axis=0)
temp_data_one = {'country': df.country, 'year': df.year, 'population': df.population}
new_data_one = pd.DataFrame(df)

sns.set(style="whitegrid")

g = sns.catplot(x="year", y="population", hue="country", data=new_data_one, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("Population")

fig = plt.figure()
fig.add_subplot(111)
fig.add_subplot()

#############
# Chart Two #
#############

sns.set(style="whitegrid")

df = {'Greece': greece.population.tolist(), 'Germany': germany.population.tolist(), 'France': france.population.tolist()}
df_new = pd.DataFrame(data=df, index=greece.year.tolist())

plt.subplot(222)
plt.subplot(sns.lineplot(data=df_new, palette="tab10", linewidth=2.5))

###############
# Chart Three #
###############

sns.set()

df = pd.concat([greece, germany, france], axis=0)
temp_data = {'country': df.country, 'year': df.year, 'population': df.population}
new_data = pd.DataFrame(df)

palette_style = sns.cubehelix_palette(rot=-.2, as_cmap=True)

plt.subplot(212)
plt.subplot(sns.scatterplot(x="population", y="year", style="country", palette=palette_style, data=new_data))

plt.show()
