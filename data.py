
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\6-1\Assay Lines Test MIQ20 and MIQ21.xlsx'
df = pd.read_excel(Workbook1)

dfmelt = pd.melt(df, id_vars=['time'],
                    var_name='Instrument',
                    value_name='Pressure')
dfmelt=dfmelt.dropna()
sns.lineplot(data=dfmelt, x='time', y='Pressure', hue="Instrument")
plt.title("Pressure Tests")
plt.xlabel("Time")
plt.ylabel("Pressure (Psi)")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)