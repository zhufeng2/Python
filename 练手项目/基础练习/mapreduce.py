def is_palindrome(s):
    s=str(s)
    return s==s[::-1]
b=filter(is_palindrome,range(1,1000))
print(list(b))