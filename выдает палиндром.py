def palindrome ([str]):
str = 'Мороз в узел, лезу взором'
str = str.replace(' ','').lower()
rev = reversed(str)
if list(str) == list(rev):
    print('Палиндром')
else:
    print('Не палиндром')   
    