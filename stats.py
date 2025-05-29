#import statistics
#print(statistics.mean([100,90]))

import sys

if len(sys.argv) < 2:
    sys.exit("too few args")
#check pypi.org
for arg in sys.argv[1:]:#use negative numbers to slice from the end of a list
    print("Hello, my name is", arg)
