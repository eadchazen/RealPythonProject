import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Plug Size data\PumpSwap.xlsx'

df_x = pd.read_excel(Workbook1)


sns.scatterplot(data= df_x, x='Plug Number ', y='Plug size ', hue='New Pump ', style ='Instrument ')
plt.ylim(0,4.5)
plt.title('Small Volume Aspirate Chart')
plt.xlabel("Location")
plt.ylabel("Small Volume Aspirate Volume (uL)")

