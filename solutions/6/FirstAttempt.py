# Pretty straightforward solution comes to mind using loops 
# sum1 = sum of the squaures 
# sum2 = square of the sum

sum1 = 0
sum2 = 0
n = 100
for i in range(1,n+1):
    sum1 += i**2
    sum2 += i

print((sum2**2)-sum1)