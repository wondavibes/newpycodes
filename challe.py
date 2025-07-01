from index import find_index
def main(): 
    Listname = ["BoluNinalowo", "Hakeem", "Buju", "Obaniyi"]
    chrc = input("enter a character :")
    for name in Listname:
        location = find_index(name, chrc.casefold)
        if location:
            print(f"the letter '{chrc}' is found at indices: '{location}'")
        else:
            print(f"character '{chrc}' not found")
    


"""def locate(name, chrc):
    pos = name.find(chrc)
    return (pos + 1)"""

if __name__ == "__main__":
    main()


#print(f" {name} has {hands} hands and {legs} legs")
   # hands = 4
#legs = 2
