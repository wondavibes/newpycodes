import re

name = input("what's your name? ")
if match := re.search(r"^(.+), *(.+)$", name):
    name = match.group(2) + " " + match.group(1)
print(f"hello, {name}")


#:=(walrus) is an operator for assigning values and asking an if statement on the same line
