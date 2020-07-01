#1
parrot = "Norwegian Blue"
for character in parrot:
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(character)

#2

for i in range (0,100,7):
    print(i)

#3
for i in range (1,11):
    for j in range (1,11):
        print("{0} times {1} is {2}".format(j,i,i*j))
    print("- "* 10)

