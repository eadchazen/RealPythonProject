
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-24\MainNegative Pressure testing21.xlsx'
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-18\MainNegative Pressure testing20.xlsx'
#output_work =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-24\output.xlsx'
df_Workbook1 = pd.read_excel(Workbook1)
df_Workbook2 = pd.read_excel(Workbook2)

#print(df_Workbook2.columns)
#print(df_Workbook1.columns)
df_3= df_Workbook1.merge(df_Workbook2, left_on ='MIQ21 -Baseline', right_on ='MIQ20-Baseline')


dfmelt = pd.melt(df_3, id_vars=['time_x'],
                    var_name='Instrument',
                    value_name='Pressure')
dfmelt=dfmelt.dropna()
sns.lineplot(data=dfmelt, x='time', y='Pressure', hue="Instrument")
plt.title("Pressure Tests")
plt.xlabel("Time")
plt.ylabel("Pressure (Psi)")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)

