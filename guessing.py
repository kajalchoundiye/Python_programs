answer = 5
print("please guess number between 1 to 10")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("please guess lower")
else:
    print("you got it first time")