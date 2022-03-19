import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
fig, ax = plt.subplots()

fig = df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', figsize=(6, 6))

plt.title('Rise in the sea level')

a = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x = []
for i in range(1880, 2051):
    x.append(i)
x = pd.Series(x)
y = a.intercept + a.slope * x
plt.plot(x, y, 'm')

df2 = df.loc[df['Year'] >= 2000]
a = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
x = []
for i in range(2000, 2051):
    x.append(i)
x = pd.Series(x)
y = a.intercept + a.slope * x
plt.plot(x, y, 'y')

ax.set_ylabel('Sea level (inches)')
ax.set_xlabel('Year')
ax.set_title('Rise in the sea level')