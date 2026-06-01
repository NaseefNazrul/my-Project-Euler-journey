prev = 1
curr = 1
n = 4000000
sum = 0

while curr <= n:

    if curr % 2 == 0: 
        sum += curr
    temp = curr
    curr = curr + prev
    prev = temp

print(sum)