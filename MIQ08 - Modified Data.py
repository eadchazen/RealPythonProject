import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 1.csv' #Run 1 6-18 9:33 - air on chip
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 2.csv' #Run 2 6-18 12:48 - half sized plug one and two
Workbook3 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 3.csv' #Run 3 6-18 15:36 - Mostly normal looking run
Workbook4 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 4.csv' #Run 4 6-28 14:19
Workbook5 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 5.csv' #full run data 23058: 2022-06-18 09:33
Workbook6 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 6.csv' #full run data 2022-06-18 12:48:37.558
Workbook7 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 7.csv' #full run data 23827: 2022-07-06 09:09
Workbook8 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 8.csv' #Prime data 6-16
Workbook9 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 6 .csv' #Prime Data MIQ20
Workbook10 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 10.csv' #23956: 2022-07-09 12:37
Workbook11 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ20\MIQ20 - Run 5 .csv' #23830: 2022-07-06 09:11
Workbook12 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 11.csv' #23990: 2022-07-10 12:52
Workbook13 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ8\MIQ8 - 6-18 run 9.csv' #23990: 2022-07-10 12:52
data = [Workbook13]

runcount = 1
dataframes1=[]

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
#axes[0].set_xlim([0,.7e12])
sns.lineplot(data= df_6, x='tick', y='sensor_reading', hue = 'run',ax = axes[1])
axes[1].set_title('Sample')
#axes[1].set_xlim([0,.7e12])
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")
#plt.xlim([0,.7e12])