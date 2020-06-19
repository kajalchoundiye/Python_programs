answer = 5
print("please guess number between 1 to 10:")
guess=int(input())

if guess!=answer:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess == answer:
        print('well done..')
    else:
        print("sorry")
else:
    print("yot got it")