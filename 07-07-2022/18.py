
def ispallindrome(str):
    l = len(str)
    for i in range(len(str)//2):
        if str[i] == str[l-i-1]:
            continue
        else:
            return False
    return True    

print(ispallindrome(""))

