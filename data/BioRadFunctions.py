
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def graphbioradct(dataframe, xvar):
    df_2 = dataframe[(dataframe.Filter == 'Quasar 705')]
    df_3 = dataframe[(dataframe.Filter == 'Texas Red')]
    df_4 = dataframe[(dataframe.Filter == 'FAM')]
    df_5 = dataframe[(dataframe.Filter == 'Cy5')]

    fig, axes = plt.subplots(nrows=2, ncols=2)
    sns.stripplot(data=df_2, x=xvar, y='CT', ax=axes[0, 0], hue=xvar, palette='bright')
    axes[0, 0].set_title('Quasar 705 -CT')
    sns.stripplot(data=df_3, x=xvar, y='CT', ax=axes[1, 0], hue=xvar, palette='bright')
    axes[1, 0].set_title('Texas Red -CT')
    sns.stripplot(data=df_4, x=xvar, y='CT', ax=axes[0, 1], hue=xvar, palette='bright')
    axes[0, 1].set_title('FAM -CT')
    sns.stripplot(data=df_5, x=xvar, y='CT', ax=axes[1, 1], hue=xvar, palette='bright')
    axes[1, 1].set_title('Cy5 -CT')




def graphbioraddrfu(dataframe,xvar):
    df_2 = dataframe[(dataframe.Filter == 'Quasar 705')]
    df_3 = dataframe[(dataframe.Filter == 'Texas Red')]
    df_4 = dataframe[(dataframe.Filter == 'FAM')]
    df_5 = dataframe[(dataframe.Filter == 'Cy5')]

    fig, axes = plt.subplots(nrows=2, ncols=2)
    sns.stripplot(data=df_2, x=xvar, y='dRFU', ax=axes[0, 0], hue=xvar, palette='bright')
    axes[0, 0].set_title('Quasar 705 -dRFU')
    sns.stripplot(data=df_3, x=xvar, y='dRFU', ax=axes[1, 0], hue=xvar, palette='bright')
    axes[1, 0].set_title('Texas Red -dRFU')
    sns.stripplot(data=df_4, x=xvar, y='dRFU', ax=axes[0, 1], hue=xvar, palette='bright')
    axes[0, 1].set_title('FAM -dRFU')
    sns.stripplot(data=df_5, x=xvar, y='dRFU', ax=axes[1, 1], hue=xvar, palette='bright')
    axes[1, 1].set_title('Cy5 -dRFU')