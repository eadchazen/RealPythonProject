import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a dataframe
targetfile = r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-9\MIQ21\2022-05-06 14.06.59.060000 -5ul before 10ul after PCR line\PressureData.csv'


logger.debug(f'Columns in loaded df are:\n{df.columns}')

# Initial attempts at plotting this data with seaborn are SLOWWWWWW.......
sns.lineplot(data=df, x='tick', y='pressure_value', hue='sensor_id')

# Let's start exploring why
# Method 1: cull "inappropriate" data
# the method .describe() can be used to get stats for a group and/or column
stats = df.groupby('sensor_id')['pressure_value'].describe()
logger.debug(f'Stats for pressure by id:\n{stats}')

# The sensor data saved in sensor_id == 3 appears invalid, let's start by filtering it out
sensor2df = df[df['sensor_id'] == 2]

# Plotting a line plot is..... still slow
sns.lineplot(data=sensor2df, x='tick', y='pressure_value', hue='sensor_id')

# Lets take a look at the data types in our dataframe
logger.debug(f'Data Types:\t{sensor2df.dtypes}')
# "tick" is listed as an "object", which can be thought of as a string

# Using the "iloc" function, we can get the first (or any) entry in our datafram
# Let's take a look and determine whether there is a better datatype for "tick"
logger.debug(f'{sensor2df.iloc[0]}')

# Based on this, "tick" looks like a date / time value
# Let's cast this column as a pandas "datetime64" type to significantly improve performance
sensor2df['tick'] = sensor2df['tick'].astype('datetime64[ns]')

# Let's try plotting again
_, ax = plt.subplots()
sns.lineplot(data=sensor2df, x='tick', y='pressure_value', hue='sensor_id', ax=ax)