
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stat

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Biorad\Premix experiment.xlsx'
df_1 = pd.read_excel(Workbook1)
print(df_1)

df_1 = df_1[(df_1.Tube != 'Empty')]
df_1 = df_1[(df_1.Tube != '#N/A')]
df_1 = df_1[(df_1.Tube != 'N/A')]

df_1 = df_1[(df_1.Instrument != 'Control -1 ')]
df_1 = df_1[(df_1.Instrument != 'Control -2')]
df_1 = df_1[(df_1.Instrument != 14)]

df_2 = df_1[(df_1.Filter == 'Quasar 705')]
df_3 = df_1[(df_1.Filter == 'Texas Red')]
df_4 = df_1[(df_1.Filter == 'FAM')]
df_5 = df_1[(df_1.Filter == 'Cy5')]

print(df_1)

fig, axes = plt.subplots(nrows=2, ncols=2)
sns.stripplot(data= df_2, x='Instrument', y = 'CT',  ax = axes[0, 0], hue='Instrument', palette ='bright')
axes[0, 0].set_title('Quasar 705 -CT')
sns.stripplot(data= df_3, x='Instrument', y = 'CT', ax = axes[1, 0 ],  hue='Instrument', palette ='bright')
axes[1, 0].set_title('Texas Red -CT')
sns.stripplot(data= df_4, x='Instrument', y = 'CT',  ax = axes[0, 1], hue='Instrument', palette ='bright')
axes[0,1].set_title('FAM -CT')
sns.stripplot(data= df_5, x='Instrument', y = 'CT',  ax = axes[1, 1], hue='Instrument', palette ='bright')
axes[1,1].set_title('Cy5 -CT')



fig, axes = plt.subplots(nrows=2, ncols=2)
sns.stripplot(data= df_2, x='Instrument', y = 'dRFU',  ax = axes[0, 0], hue='Instrument', palette ='bright')
axes[0, 0].set_title('Quasar 705 -dRFU')
sns.stripplot(data= df_3, x='Instrument', y = 'dRFU', ax = axes[1, 0 ],  hue='Instrument', palette ='bright')
axes[1, 0].set_title('Texas Red -dRFU')
sns.stripplot(data= df_4, x='Instrument', y = 'dRFU',  ax = axes[0, 1], hue='Instrument', palette ='bright')
axes[0,1].set_title('FAM -dRFU')
sns.stripplot(data= df_5, x='Instrument', y = 'dRFU',  ax = axes[1, 1], hue='Instrument', palette ='bright')
axes[1,1].set_title('Cy5 -dRFU')

















# plt.figure(0)
# sns.catplot(data= df_2, x='Instrument', y = 'CT',  hue='Instrument', palette ='bright')
# plt.suptitle('Quasar 705 -CT')
#
# plt.figure(1)
# sns.catplot(data= df_3, x='Instrument', y = 'CT',  hue='Instrument', palette ='bright')
# plt.suptitle('Texas Red -CT')
#
# plt.figure(2)
# sns.catplot(data= df_4, x='Instrument', y = 'CT',  hue='Instrument', palette ='bright')
# plt.suptitle('FAM -CT')
#
# plt.figure(3)
# sns.catplot(data= df_5, x='Instrument', y = 'CT',  hue='Instrument', palette ='bright')
# plt.suptitle('Cy5 -CT')
#
#
# plt.figure(4)
# sns.catplot(data= df_2, x='Instrument', y = 'dRFU',  hue='Instrument', palette ='bright')
# plt.suptitle('Quasar 705 -dRFU')
#
# plt.figure(5)
# sns.catplot(data= df_3, x='Instrument', y = 'dRFU',  hue='Instrument', palette ='bright')
# plt.suptitle('Texas Red -dRFU')
#
# plt.figure(6)
# sns.catplot(data= df_4, x='Instrument', y = 'dRFU',  hue='Instrument', palette ='bright')
# plt.suptitle('FAM -dRFU')
#
# plt.figure(7)
# sns.catplot(data= df_5, x='Instrument', y = 'dRFU',  hue='Instrument', palette ='bright')
# plt.suptitle('Cy5 -dRFU')
