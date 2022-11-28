
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\Plug movement baseline.xlsx')


sns.scatterplot(data=df, x='Instrument ', y='Plug Movement', hue='Status')

plt.title("Plug Movement")
plt.xlabel("Instrument ")
plt.ylabel("Plug Movement")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\Pressure testing\4-27\Copy of MiQ-21 Assay and Sample side MPSDecon3.xlsx')


sns.scatterplot(data=df, x='time', y='Plug Movement', hue='Status')

plt.title("Plug Movement")
plt.xlabel("time")
plt.ylabel("Plug Movement")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)