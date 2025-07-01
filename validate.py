import re

email = input("what's your email? ").strip()
pattern = r"^\w+@(?:(\w+)\.)?\w+\.(org|com|edu|net)$"
if valid := re.search(pattern, email, re.IGNORECASE):

    print("valid", valid.group(1))
else:
    print("invalid")


""" [^@] means no @ sign is wanted before and after the only @."""
# \.edu$ means the user must enter a literal dot(.) 
#after some characters post the @ sign and the input must end with .edu
#using [] would define a set of allowed characters unlike [^]. Use \w to specify alphanumeric characters
# and underscore. (org|edu|com|net)$ allows for more domain endings. sub domains are doable with extra (\w+\.)?