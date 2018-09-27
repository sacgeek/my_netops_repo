import re
namestring = False

while namestring is False:
    name = input("Hey person, what is your name? ")
    x = re.search('[0-9]', name)
    if x:
        namestring = False
    else:
        namestring = True
        print(name)
