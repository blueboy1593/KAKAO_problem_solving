my_dict = {'a' : { 'b': { 'c': {} } } }
if my_dict.get('a'):
    print(True)
print(my_dict['a'])
print(type(my_dict['a']))
if my_dict['a'].get('b'):
    print('aseff')
else:
    print('Nooo')

# my_dict.update