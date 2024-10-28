
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



weatherData = pd.read_csv('C:/Users/ritik/Downloads/weatherHistory.csv.zip')


print(weatherData.head())
print(weatherData.info())
print(weatherData.describe())


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature (C)', y='Humidity', data=weatherData,color="yellow")
plt.title('Humidity vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity')
plt.show()


plt.figure(figsize=(10, 6))
sns.jointplot(x='Temperature (C)', y='Humidity', data=weatherData, kind='hex',color="green")
plt.suptitle('Joint Distribution of Temperature and Humidity', y=1.02)
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity')
plt.show()
