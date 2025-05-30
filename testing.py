#test.py

import re

unletter = input("enter a weird email :").strip()
pattern = r"^\W+@(?:\w+\.com)"

if re.search(pattern, unletter, re.IGNORECASE):
    print("VALID")
else:
    print("invalid")