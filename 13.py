def isprime(num):
    count=1

    for i in range(1,num):
        if(num%i==0):
            count +=1

    if count > 2:
        return False
    else:
        return True

for i in range(9,100):
    if isprime(i) is True:
        print(i)

