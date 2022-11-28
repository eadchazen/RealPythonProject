
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\MIQ8 - 6-18 run 1.csv'
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\MIQ8 - 6-18 run 2.csv'
Workbook3 =r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\MIQ8 - 6-18 run3.csv'
#output_work =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-24\output.xlsx'
df_1 = pd.read_csv(Workbook1)
df_2 = pd.read_csv(Workbook2)
df_3 = pd.read_csv(Workbook3)

dataframes = [df_1, df_2, df_3]

df_4 = pd.concat(dataframes, ignore_index=True,)

#join.to_excel(r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\Output.xlsx'
#Workbook4 =r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\Output.xlsx'
#df_4 = pd.read_excel(Workbook4)
#df_5.dtypes
df_4['tick'] = df_4['tick'].astype('datetime64[ns]')
df_4 = df_4[(df_4.sensor_id > 10.1)]

sns.lineplot(data= df_4, x='tick', y='sensor_reading')

plt.title("ADC Sensor Reading")
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")
