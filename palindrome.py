def is_palindrome(s):
    left=0
    right=len(s)-1
    while left <right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
        return True
word = input("Enter a word")
if is_palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")