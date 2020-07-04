Numbers = [1, 15, 25, 678, 89]

for number in Numbers:
    if number % 8==0:
        print("The numbers are unaccetable")
        break

else:
    print("This all numbers are fine..!")