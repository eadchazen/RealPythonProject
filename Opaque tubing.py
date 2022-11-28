import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\opaque tubing\Opaque tubing.xlsx'

df_x = pd.read_excel(Workbook1)

# CT
sns.scatterplot(data= df_x, x='Plug Number ', y='CT', hue='Tubing ')
plt.ylim(0)
plt.title('Tubing Opaqueness')
plt.xlabel("Plug Number")
plt.ylabel("CT")


# Score
sns.scatterplot(data= df_x, x='Plug Number ', y='Score', hue='Tubing ')
plt.ylim(0)
plt.title('Tubing Opaqueness')
plt.xlabel("Plug Number")
plt.ylabel("Score")


# DeltaRFU
sns.scatterplot(data= df_x, x='Plug Number ', y='DeltaRFU', hue='Tubing ')
plt.ylim(0)
plt.title('Tubing Opaqueness')
plt.xlabel("Plug Number")
plt.ylabel("DeltaRFU")