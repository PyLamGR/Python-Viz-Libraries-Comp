import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from myPlotter import myPlotter

data = pd.read_csv('countries.csv')

greece = data[data.country == 'Greece']
germany = data[data.country == 'Germany']
france = data[data.country == 'France']


fig, ax = plt.subplots(2, 2)

ax[0, 0].set_title('Population growth comparison.')

ax[0, 0].plot(greece.year, greece.population / 10**6, label='Greece')
ax[0, 0].plot(germany.year, germany.population / 10**6, label='Germany')
ax[0, 0].plot(france.year, france.population / 10**6, label='France')

ax[0, 0].legend()

ax[0, 0].set_xlabel('Year')
ax[0, 0].set_ylabel('Population (in millions)')



ax[0, 1].set_title('Precentage of Total population per Country.')

totalPopulation = int(greece.population.tail(1)) + int(germany.population.tail(1)) + int(france.population.tail(1))

greekPrecentage = (int(greece.population.tail(1)) * 100 / totalPopulation)
germanyPrecentage = (int(germany.population.tail(1)) * 100 / totalPopulation)
francePrecentage = (int(france.population.tail(1)) * 100 / totalPopulation)

labels = 'Greece', 'Germany', 'France'
sizes = [greekPrecentage, germanyPrecentage, francePrecentage]

ax[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax[0, 1].axis('equal')

###########
# CHART 3 #
###########

ax[1, 0].set_title('Population of Greece 1987-2007.')

xPos = np.arange(len(greece.year.tail()))

ax[1, 0].bar(xPos, greece.population.tail()/10**6, align='center', width=0.35)

ax[1, 0].set_xticks(xPos)
ax[1, 0].set_xticklabels(greece.year.tail())

ax[1, 0].set_ylim(top=12)

ax[1, 1].set_title('Chart 4.')

plt.show()