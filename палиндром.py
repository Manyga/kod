def is_palindrome(s):
    s = s.replace(' ','').lower()
    return s == s[::-1]
string = 'Do geese see God'
if  is_palindrome(string):
    print('Palindrome')
else:
    print ('Not palindrome')
  

