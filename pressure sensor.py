
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Let's work with the following example file:
targetfile = r'N:'\Product Development\Lexagene Engineering\elana\Pressure testing\4-27\Copy of MiQ-21 Assay and Sample side MPSDecon3.xlsx'

# Load data into a dataframe
df = pd.read_excel(targetfile)

stats = df.groupby('sensor_id')['pressure_value'].describe()
logger.debug(f'Stats for pressure by id:\n{stats}')
sensor2df = df[df['sensor_id'] == 2]
sns.lineplot(data=sensor2df, x='tick', y='pressure_value', hue='sensor_id')