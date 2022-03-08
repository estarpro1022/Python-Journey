def reverse(text):
    return text[::-1]

def isPalindrome(text):
    return text == reverse(text)

list = input('Enter a list: ')

if isPalindrome(list):
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')

