names = []
# alt version-- skip the list[] creation and use for line in sorted(file) then print hello and line with strip method
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #r.strip is necesssary to avoid double spaces between print statements

for name in sorted(names, reverse=False):
    print(f"hello, {name}")
