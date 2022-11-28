"""
Training Module 2: Helpful libraries with their "default" import statements, used widely throughout training module
Written by: Scott Kelley
Date: 17 March 2022
"""


"""
os: default python library, used for interacting with OS objects
WARNING: this is OS specific, if you're in a NON-WINDOWS environment, some small issues may occur
"""
import os

"""
re: default python library, used for regular expression handling
NOTE: regular expressions are awesome, but esoteric at the same time, confusion is *normal*
Explanatory resource: https://docs.python.org/3/howto/regex.html
Interactive resource: https://regexr.com/
"""
import re


"""
loguru: simple logger supporting semi complex out of the box behavior
https://github.com/Delgan/loguru
"""
from loguru import logger
logger.debug('This is a debug message')
x = 4
logger.debug(f'This is a message with an f-string. The value of x is {x}')

"""
numpy: numerical data handling and calculation
https://numpy.org/
"""
import numpy as np
newarray = np.arange(15)
logger.debug(f'Check it out, here\'s an array: {newarray}')

"""
pandas: data handling and processing
https://pandas.pydata.org/
"""
import pandas as pd
d = {'col1': [1, 2, 4, 8, 16], 'col2': [1, 2, 3, 4, 5]}  # Create a dictionary with data, each "key" will be a column, each "value" list will be data in the column
df = pd.DataFrame(data=d)  # Create dataframe from dictionary
logger.debug(f'Newly created dataframe:\n{df}')

"""
matplotlib: Data visualization
https://matplotlib.org/
"""
import matplotlib.pyplot as plt
logger.debug('Plotting our df...')
plt.figure()  # Create a figure object
plt.plot(df['col1'], df['col2'])  # Plot (line plot) data to the new figure, default args are x, y
plt.title('Plotting our Dataframe')  # Put a title on the plot
plt.xlabel('X Axis Label')  # Label the x-axis
plt.ylabel('Y Axis Label')  # Label the y-axis
plt.show()  # Show the plot


"""
seaborn: enhanced wrapper for matplotlib, makes prettier plots faster
https://seaborn.pydata.org/
"""
import seaborn as sns
sns.scatterplot(data=df, x='col1', y='col2')  # Create a scatter plot from dataframe
plt.title('Plotting our Dataframe')  # Put a title on the plot
plt.xlabel('X Axis Label')  # Label the x-axis
plt.ylabel('Y Axis Label')  # Label the y-axis
