
num = input("enter num")
rev =""
for i in reversed(range(len(num))):
    rev += num[i]
print(rev)