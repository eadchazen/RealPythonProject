import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ41\MIQ41 - ADC Data with BulkMoveChains.csv' #BulkMoveChains
Workbook2 =r'N:\Product Development\Lexagene Engineering\elana\ADC\MIQ41\MIQ41 - ADC Data without BulkMoveChains.csv' #With out BulkMoveChains
data = [Workbook1, Workbook2]

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
sns.lineplot(data= df_5, x='tick', y='sensor_reading', hue = 'run',ax = axes[0])
axes[0].set_title('Assay')
axes[0].set_xlim([0,.7e12])
axes[0].set_ylim([0,2.1])
sns.lineplot(data= df_6, x='tick', y='sensor_reading', hue = 'run',ax = axes[1])
axes[1].set_title('Sample')
axes[1].set_xlim([0,.7e12])
axes[1].set_ylim([0,2.1])
plt.xlabel("Tick")
plt.ylabel("Sensor Reading")
#plt.xlim([0,.7e12])