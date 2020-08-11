# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/Assets/us-counties.csv')

df0 = df[(df["county"] == 'Alachua') & (df["state"] == 'Florida')]
df00 = df0[['date','cases']]
df00.to_csv('/Assets/Cases/alachuacases.csv', index = False)

df1 = df[(df["county"] == 'Broward') & (df["state"] == 'Florida')]
df01 = df1[['date','cases']]
df01.to_csv('/Assets/Cases/browardcases.csv', index = False)

df2 = df[(df["county"] == 'Hillsborough') & (df["state"] == 'Florida')]
df02 = df2[['date','cases']]
df02.to_csv('/Assets/Cases/hillsboroughcases.csv', index = False)

df3 = df[(df["county"] == 'Leon') & (df["state"] == 'Florida')]
df03 = df3[['date','cases']]
df03.to_csv('/Assets/Cases/leoncases.csv', index = False)

df4 = df[(df["county"] == 'Miami-Dade') & (df["state"] == 'Florida')]
df04 = df4[['date','cases']]
df04.to_csv('/Assets/Cases/miamidadecases.csv', index = False)

df6 = df[(df["county"] == 'Monroe') & (df["state"] == 'Florida')]
df05 = df6[['date','cases']]
df05.to_csv('/Assets/Cases/monroecases.csv', index = False)

df7 = df[(df["county"] == 'Orange') & (df["state"] == 'Florida')]
df06 = df7[['date','cases']]
df06.to_csv('/Assets/Cases/orangecases.csv', index = False)

df8 = df[(df["county"] == 'Osceola') & (df["state"] == 'Florida')]
df07 = df8[['date','cases']]
df07.to_csv('/Assets/Cases/osceolacases.csv', index = False)

df9 = df[(df["county"] == 'Palm Beach') & (df["state"] == 'Florida')]
df08 = df9[['date','cases']]
df08.to_csv('/Assets/Cases/palmbeachcases.csv', index = False)

df10 = df[(df["county"] == 'Pinellas') & (df["state"] == 'Florida')]
df09 = df10[['date','cases']]
df09.to_csv('C/Assets/Cases/pinellascases.csv', index = False)

frames = [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]

data = pd.concat(frames)


#ALACHUA COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(df0.index.values,
        df0['cases'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Alachua County from March to May 2020")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)
plt.savefig('alachuacases.png')
plt.show()


#BROWARD COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df1.index.values,
        df1['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Broward County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('browardcases.png')
plt.show()


#HILLSBOROUGH COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df2.index.values,
        df2['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Hillsborough County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)
plt.savefig('hillsboroughcases.png')
plt.show()


#LEON COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df3.index.values,
        df3['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Leon County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('leoncases.png')
plt.show()


#MIAMI-DADE COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df4.index.values,
        df4['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Miami-Dade County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('miamidadecases.png')
plt.show()


#MONROE COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df6.index.values,
        df6['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Monroe County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('monroecases.png')
plt.show()



#ORANGE COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df7.index.values,
        df7['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Orange County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('orangecases.png')
plt.show()



#OSCEOLA COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df8.index.values,
        df8['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Osceola County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('osceolacases.png')
plt.show()


#PALM BEACH COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df9.index.values,
        df9['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Palm Beach County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('palmbeachcases.png')
plt.show()


#PINELLAS COUNTY
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(df10.index.values,
        df10['cases'],
        color='purple')

ax.set(xlabel="Date",
       ylabel="Cases",
       title="Daily Total Cases, Pinellas County from March to May 2020")

plt.setp(ax.get_xticklabels(), rotation=45)

plt.savefig('pinellascases.png')
plt.show()
































