
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data.definitions import dataanaylsis
import scipy.stats as f_oneway

df_1 = pd.read_excel(r'N:\Product Development\Lexagene Engineering\elana\Pumptesting.xlsx')


dataanaylsis(df_1, 'Percent Error ', 'Pumps', 1)



df_2 = df_1[(df_1.Pump == '40 Bad')]
df_3 = df_2["Percent Error "].tolist()
print (df_3)
#
#
df_4 = df_1[(df_1.Pump == '46 Bad')]
df_5 = df_4["Percent Error "].tolist()
print (df_5)
#
#
# df_6 = df_1[(df_1.Pump == '48 Bad ')]
# df_7 = df_6["Percent Error "].tolist()
#
# print (df_7)

# p = f_oneway(df_5, df_7)
#
# plt.figure(1)
# sns.histplot(data= df_2, x='Percent Error ', hue ='Pump', binwidth = 1)
# plt.show()
#
#
# plt.figure(2)
# sns.histplot(data= df_4, x='Percent Error ', hue ='Pump', binwidth = 1)
# plt.show()

# stats.f_oneway()


# filter by another column
# configurable program in python for data analysis