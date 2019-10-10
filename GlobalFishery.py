"""%python
import os
from pip._internal import main
import sys

# work around the lack of tty in the interpreter
sys.stdout.isatty = lambda : False
sys.stdout.encoding = None

main(["install", "--user", "-U", "matplotlib", "numpy", "pandas"])"""

import pandas as pd

# first I added a new column for total values
third = pd.read_csv('https://www.dropbox.com/s/je8t9udv1vs8isw/global-fishery-catch-by-sector.csv?&raw=1')
sec = third.plot(x = 'Year', y = 'total', color = 'red', marker='X', kind = 'line', title = 'Global Fishery Catch')
sec.set_ylabel("Million Tonnes")
