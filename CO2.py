"""%python
import os
from pip._internal import main
import sys

# work around the lack of tty in the interpreter
sys.stdout.isatty = lambda : False
sys.stdout.encoding = None

main(["install", "--user", "-U", "matplotlib", "numpy", "pandas"])"""

import pandas as pd
import matplotlib.pyplot as plt
second = pd.read_csv('https://www.dropbox.com/s/qduukco66kb3hp7/global-co-concentration-ppm.csv?&raw=1')
sec = second.plot(x = 'Year', y = 'CO2', color = 'red', marker='X', kind = 'line', title = 'Global Carbon Dioxide Atmospheric Concentration')
sec.set_ylabel("parts per million (ppm)")
