#/usr/bin/env python3

import sys
import time

for i in range(5):
    sys.stdout.write('Processing {}\n'.format(i))
    time.sleep(1)

for i in range(5):
    sys.stderr.write('Error {}\n'.format(i))
    time.sleep(1)

