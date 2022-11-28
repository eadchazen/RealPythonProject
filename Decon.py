
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\Decon testing\Decon Plug to Plug CarryOver.xlsx')


scatter= sns.lineplot(data=df, x='Run type', y='Plug 3 Score ', hue='Instrument ')
scatter.legend(bbox_to_anchor= (1.13, 1) );

plt.title("Plug 3 Staph Plug to Plug Carry Over")
plt.xlabel("Run Type")
plt.ylabel("Score")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\Decon testing\Decon Plug to Plug CarryOver.xlsx')


scatter = sns.scatterplot(data=df, x='Run type', y='Plug 9 Score ', hue='Instrument ')
scatter.legend(bbox_to_anchor= (1.12, 1) );

plt.title("Plug 9 Ecoli Plug to Plug Carry Over")
plt.xlabel("Run Type")
plt.ylabel("Score")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\MIQ20 - Decon.xlsx')



dfmelt = pd.melt(df, id_vars=['tick'],
                    var_name='Instrument',
                    value_name='Pressure')
dfmelt=dfmelt.dropna()
sns.lineplot(data=dfmelt, x='tick', y='Pressure', hue="Instrument")
plt.title("Pressure Tests")
plt.xlabel("Time")
plt.ylabel("Pressure (Psi)")
#df.plot(kind='scatter', x='time', y='MIq11', figsize=(12,6))
#print(df)