count = 1
num = 3 
prime = True
while count != 10001:
    prime = True
    print(num)
    if num % 2 != 0: 
        for i in range(2,num//2+1):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            count+= 1
            num += 2
        else:
            num += 2
    else: 
        num += 2

print(num-2) # Gets updated extra