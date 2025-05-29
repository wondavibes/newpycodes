"""import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.say("hello, " + sys.argv[1])"""

import cowsay
import sys

if hasattr(cowsay, 'cowsay'):
    print("The 'cowsay' attribute exists in the cowsay module.")
else:
    print("The 'cowsay' attribute does not exist in the cowsay module.")
