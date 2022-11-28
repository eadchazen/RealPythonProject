
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def dataanaylsis(dataframe, measurement, variable, binwidth):
    plt.figure(0)
    sns.histplot(data=dataframe, x=measurement, hue=variable, binwidth=binwidth)
    plt.figure(1)
    sns.stripplot(data=dataframe, x=variable, y=measurement, hue=variable)
    plt.figure(2)
    sns.boxplot(data=dataframe, x=variable, y=measurement, hue=variable)
