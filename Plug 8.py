
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stat

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\other\Plug 8.xlsx'
df_1 = pd.read_excel(Workbook1)
print(df_1)


fig, axes = plt.subplots(nrows=3, ncols=1)
sns.scatterplot(data= df_1, x='Instrument ', y = 'CT', ax = axes[0], hue='Instrument ', palette ='bright')
axes[0].set_title('Plug 8 CT')
axes[0].set_ylim([0,50])
axes[0]._remove_legend("upper left")

sns.scatterplot(data= df_1, x='Instrument ', y = 'dRFU', ax = axes[1],  hue='Instrument ', palette ='bright' )
axes[1].set_title('Plug 8 dRFU')
axes[1].set_ylim([0,50])
axes[1]._remove_legend("upper left")

sns.scatterplot(data= df_1, x='Instrument ', y = 'Score', ax = axes[2], hue='Instrument ', palette ='bright')
axes[1].set_title('Plug 8 Score')
axes[2].set_ylim([0,50])
