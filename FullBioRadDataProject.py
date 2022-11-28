import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stat
from data.BioRadFunctions import graphbioradct, graphbioraddrfu

Workbook1 =r'N:\Product Development\Lexagene Engineering\elana\Biorad\BioRad Data with IAC exploration (15Feb2022) - Data Processing NEW.xlsx'
df_1 = pd.read_excel(Workbook1, sheet_name='4) Complete Dataset')
print(df_1)

df_1 = df_1[(df_1.Tube != 'Empty')]
df_1 = df_1[(df_1.Tube != '#N/A')]
df_1 = df_1[(df_1.Tube != 'N/A')]

# df_1 = df_1[(df_1.Instrument != 'Control -1 ')]
# df_1 = df_1[(df_1.Instrument != 'Control -2')]
# df_1 = df_1[(df_1.Instrument != 14)]

graphbioradct(df_1,'Tube')
graphbioraddrfu(df_1,'Tube')

