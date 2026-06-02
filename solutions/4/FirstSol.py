# My first intuition was to use string manupilation even though I know there should be a better solution to this
# Starting from the largest and descending iteration  


def checkPalindrome(val):
    text = str(val)
    #using 2 pointer to check palindrome
    for i in range(0,len(text)//2):
        if text[i] != text[len(text)-1-i]:
            return 0
    return 1
    

# Driver code

num = 0 

for i in range(999,0,-1):
    for j in range(999,0,-1):
        if checkPalindrome(i*j) == 1:
            if i*j > num:
                num = i*j
                break

# I know theres a better way to do this instead of n^2 time complexity 
print(num)