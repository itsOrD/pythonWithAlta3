#!/usr/bin/python3

import time
import sys

for i in range(10):
    sys.stdout.write("\r{0}>".format("="*i))
    sys.stdout.flush()
    time.sleep(0.5)

print()
