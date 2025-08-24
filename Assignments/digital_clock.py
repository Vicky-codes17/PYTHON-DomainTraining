### Write the paragraph to display digital clock 

import time
import sys

h = 12
m = 60
s = 0

while(True):
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)

    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
    if m == 60:
        m = 0
        h = h + 1
    if h == 13:
        h = 1
