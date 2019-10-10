import pandas as pd
import matplotlib.pyplot as plt
#import plotly.express as px
import numpy as np
df = pd.read_csv('https://www.dropbox.com/s/hxf9ri2c5r617br/cumulative-global-plastics%281%29.csv?&raw=1')
ax = df.plot(x ='Year', y='plastic', color='red',marker='X', kind = 'scatter', title= 'Cumulative Global Plastics Production')
ax.set_ylabel("Million Tonnes of Plastic Waste")
