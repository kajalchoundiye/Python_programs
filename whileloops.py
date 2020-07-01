i = 0
while i <1:
    print("i is now {} ".format(i))
    i=i+1

available_exits = ["north","south","east","west"]

choosen_exits = True
while choosen_exits not in available_exits:
    choosen_exits = input("plz choose a direction:  ")

print("aren't you glad you got out of there")