my_int = 443
if my_int > 0:
    print("Hey, that looks like its a positive number!")
my_str = 'you call that a sentence!'
if '?' in my_str:
    print('Yup, there is a ? in that string')
elif ':' in my_str:
    print('Yup, there is a : in that string')
elif 'string' in my_str:
    print('Yup, the word string is in there...')
else:
    print('Whoa, we gota catch-all now!')
