a=[10,20,45.66,"abcd",300,199,31,"xyz"]
ans1 = a.__contains__(20)
print(ans1)
ans2 = "xyz" in a
print(ans2)
ans3 = a.index(300)
print(ans3)
print(a[-1])
print(a[:5])
print(a)
ans4 = a.remove(300)
print(a)
ans5 = a.insert(3,10)
print(a)