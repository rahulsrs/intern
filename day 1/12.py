num = int(input("enter number: "))
count=1

for i in range(1,num):
    if(num%i==0):
        count +=1

if count > 2:
    print("composite")
else:
    print("prime")

