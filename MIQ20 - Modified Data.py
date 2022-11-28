import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 1 .csv'
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 2 .csv'
Workbook3 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 3 .csv'
Workbook4 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 4 .csv' #23814: 2022-07-05 16:31
Workbook5 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 5 .csv' #23830: 2022-07-06 09:11
Workbook7 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 7 .csv' #24008: 2022-07-10 19:12
Workbook8 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 8 .csv' #23992: 2022-07-10 12:53
Workbook9 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 9 .csv' #23992: 2022-07-10 12:53
Workbook10 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 10 .csv' #23992: 2022-07-10 12:53
Workbook11 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 11 .csv' #24515: 2022-07-24 13:53
Workbook12 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 12 .csv' #24532: 2022-07-24 21:31
data = [Workbook10, Workbook12, Workbook11]

runcount = 1
dataframes1 = []

for x in data:
    df_x = pd.read_csv(x)
    df_x = df_x[(df_x.sensor_id == 11)]
    df_x['tick'] = df_x['tick'].astype('datetime64[ns]')
    tx = min(df_x.tick)
    df_x['tick'] = df_x['tick'] - tx
    df_x['run'] = runcount
    runcount = runcount + 1
    dataframes1.append(df_x)
    print(x)

#enumberate - function, variable take care of the runcount
#list comprehension

count = 1
dataframes2=[]

for x in data:
    df_x = pd.read_csv(x)
    df_x = df_x[(df_x.sensor_id == 10)]
    df_x['tick'] = df_x['tick'].astype('datetime64[ns]')
    tx = min(df_x.tick)
    df_x['tick'] = df_x['tick'] - tx
    df_x['run'] = count
    count = count + 1
    dataframes2.append(df_x)
    print(x)

#enumberate - function, variable take care of the runcount
#list comprehension

df_5= pd.concat(dataframes1, ignore_index=True)
df_6= pd.concat(dataframes2, ignore_index=True)

fig, axes = plt.subplots(nrows=2, ncols=1)
sns.lineplot(data= df_5, x='tick', y='sensor_reading', hue = 'run',ax = axes[0])
axes[0].set_title('Assay')
axes[0].set_xlim([0,.7e12])
sns.lineplot(data= df_6, x='tick', y='sensor_reading', hue = 'run',ax = axes[1])
axes[1].set_title('Sample')
axes[1].set_xlim([0,.7e12])
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")
