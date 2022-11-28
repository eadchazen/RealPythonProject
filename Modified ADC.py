
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 1.csv'
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 2.csv'
Workbook3 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 3.csv'
Workbook4 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 4.csv'
Workbook5 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 5.csv' #23736: 2022-07-03 14:39
Workbook6 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 6.csv' #23747: 2022-07-03 19:01
Workbook7 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 7.csv' #23772: 2022-07-04 09:14
Workbook8 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 8.csv' # full run 2022-07-03 14:39:18.282
Workbook9 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 9.csv' # full run 2022-07-02 15:35:51.348
Workbook10 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 10.csv' # full run 23815: 2022-07-05 16:32
Workbook11 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 11.csv' #full run 23772: 2022-07-04 09:14
Workbook12 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 12.csv' #24243: 2022-07-16 12:36
Workbook13 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 13.csv' #24259: 2022-07-16 15:37
Workbook14 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 14.csv' #24275: 2022-07-17 11:00
Workbook15 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 15.csv' #24295: 2022-07-17 16:14
Workbook16 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 16.csv' #24311: 2022-07-17 19:14
Workbook17 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 17.csv' #24311: 2022-07-17 19:14
Workbook18 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ21\MIQ21 - Run 18.csv' #24324: 2022-07-18 14:48

data = [Workbook17]

runcount = 1
dataframes1=[]

for x in data:
    df_x = pd.read_csv(x)
    df_x = df_x[(df_x.sensor_id == 16)]
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
    df_x = df_x[(df_x.sensor_id == 15)]
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
sns.lineplot(data= df_5, x='tick', y='sensor_reading', hue = 'run',ax = axes[0], palette = 'bright')
axes[0].set_title('Assay')
axes[0].set_xlim([0,.7e12])
axes[0].grid()
sns.lineplot(data= df_6, x='tick', y='sensor_reading', hue = 'run',ax = axes[1], palette = 'bright')
axes[1].set_title('Sample')
axes[1].set_xlim([0,.7e12])
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")

