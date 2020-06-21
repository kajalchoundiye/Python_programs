parrot = "Norwegian Blue"
letter = input("enter your character: ")

if letter in parrot:
    print("'{}' is in {}".format(letter,parrot))
else:
    print("i dont need that letter")
