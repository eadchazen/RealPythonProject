#MIQ20


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 1 .csv'
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 2 .csv'
Workbook3 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 3 .csv'
#output_work =r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\5-24\output.xlsx'
df_1 = pd.read_csv(Workbook1)
df_2 = pd.read_csv(Workbook2)
df_3 = pd.read_csv(Workbook3)

#df_1.columns = ['tick', 'sensor_reading', 'sensor_id']
#df_2.columns = ['tick', 'sensor_reading', 'sensor_id']
#df_3.columns = ['tick', 'sensor_reading', 'sensor_id']

df_1 = df_1[(df_1.sensor_id > 10.1)]
df_2 = df_2[(df_2.sensor_id > 10.1)]
df_3 = df_3[(df_3.sensor_id > 10.1)]

df_1['tick'] = df_1['tick'].astype('datetime64[ns]')
df_2['tick'] = df_2['tick'].astype('datetime64[ns]')
df_3['tick'] = df_3['tick'].astype('datetime64[ns]')

t1 = min(df_1.tick)
t2 = min(df_2.tick)
t3 = min(df_3.tick)

df_1['tick'] = df_1['tick']-t1
df_2['tick'] = df_2['tick']-t2
df_3['tick'] = df_3['tick']-t3

df_1['sensor_id'] = df_1['sensor_id']-0
df_2['sensor_id'] = df_2['sensor_id']-1
df_3['sensor_id'] = df_3['sensor_id']-2
dataframes = [df_1, df_2,  df_3]

#value1 = df_1[('tick1', 'sensor_reading1')]
#value2 = df_2[('sensor_reading2')]value3 = df_3[('sensor_reading3')]
df_4= pd.concat(dataframes, ignore_index=True)

#join.to_excel(r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\Output.xlsx'
#Workbook4 =r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\Output.xlsx'
#df_4 = pd.read_excel(Workbook4)
#df_5.dtypes
#df_4['tick'] = df_4['tick'].astype('datetime64[ns]')


sns.lineplot(data= df_4, x='tick', y='sensor_reading', hue = 'sensor_id')

plt.title("ADC Sensor Reading")
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")
plt.xlim([0,.7e12])
