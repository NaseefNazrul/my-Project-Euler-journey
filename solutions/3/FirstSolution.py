# at first we can do this with a normal loop but realistically it will consume wayy too much time 

factor = 2
n = 600851475143

while factor * factor <= n:
    if n % factor == 0:
        n //= factor
    else:
        factor += 1
    
print(n)