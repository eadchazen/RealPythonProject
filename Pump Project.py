import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Pump Rel Testing.xlsx'

df_x = pd.read_excel(Workbook1)

#Filtering the Data Asirate Volumes
df_x = df_x[(df_x.Apristate_Volume < 250)]
df_x = df_x[(df_x.Number_of_Dispenses < 300)]


# scatterplot

sns.scatterplot(data= df_x, x='Apristate_Volume', y='Percent Error ',hue='Pump Number ', style ='Backlash Value ')
plt.title('Pump Swaps')
plt.xlabel("Apristate Volume (ul)")
plt.ylabel("Percent Error ")

# histoplot


df_y = df_x[(df_x.Apristate_Volume == 100)]
df_y = df_y[(df_y.Number_of_Dispenses == 5)]
df_y = df_y[(df_y.Backlash_Value == 200)]


sns.histplot(data= df_y, x='Percent Error ',hue='Pump Number ',binwidth=.1)
plt.title('Pump Swaps')
plt.xlabel("Percent Error")
plt.ylabel("Frequency")

#for

AV = [5, 100]
BacklashValues = [0 , 200, 500 ]

# plt.figure(figsize=(6, 6))
for i, AV in enumerate(AV):
    print(i, AV)


# plt.tight_layout()

AspirateVolumes = [5, 100]
BacklashValues = [0 , 200, 500 ]

df_y = df_x[(df_x.Apristate_Volume == AspirateVolumes)]
df_y = df_y[(df_y.Backlash_Value == BacklashValues)]


sns.histplot(data= df_y, x='Percent Error ',hue='Pump Number ',binwidth=.1)
plt.title('Pump Swaps')
plt.xlabel("Percent Error")
plt.ylabel("Frequency")

