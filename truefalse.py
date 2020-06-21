day =  "sunday"
temperature = 30
raining = True
#1

if day=="sunday" and temperature<=30 and raining:
    print('go swimming..!')
else:
    print("try on another day..!")
print("-" * 10)
#2

if day=="monday" or temperature<=30 or raining:
    print('go swimming..!')
else:
    print("try on another day..!")
print("-" * 10)
#3

if day=="monday" or temperature<=30 and not raining:
    print('go swimming..!')
else:
    print("try on another day..!")




