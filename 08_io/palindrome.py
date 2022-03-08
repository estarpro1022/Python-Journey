def reverse(text):
    # text[::-1] 就是倒序
    return text[::-1]

text = [1, 2, 3, 2, 1]

if text == reverse(text):
    print('This is a palindrome')
else:
    print('This is not a palindrome')
