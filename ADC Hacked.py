import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\ACD\MIQ8\Assay Side Sensor.xlsx')



dfmelt = pd.melt(df, id_vars=['tick'],
                    var_name='Run Number',
                    value_name='sensor_reading')
dfmelt=dfmelt.dropna()
sns.lineplot(data=dfmelt, x='tick', y='sensor_reading', hue="Run Number")
plt.title("Sensor Reading")
plt.xlabel("Time")
plt.ylabel("Voltage Output")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)