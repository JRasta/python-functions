def flip_bool(boolean):
    if '1' in boolean or '0' in boolean:
        int(boolean)
    if 'True' in boolean:
        print(f'Boolean => 0')
    elif 'False' in boolean:
        print(f'Boolean => 1')
    elif '1' in boolean:
        print(f'Boolean => 0')
    else:
        print(f'Boolean => 1')


flip_bool('1')
flip_bool('True')
flip_bool('0')
flip_bool('False')
