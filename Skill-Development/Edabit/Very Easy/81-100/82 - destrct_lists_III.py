def destruct_lists(lst, list_item):
    count = 1
    for item in lst:
        if list_item != item:
            count = count + 1
        else:
            print(f'Item found at POS: {count} in list')


destruct_lists(['eyes', 'nose', 'lips', 'ears'], 'lips')
destruct_lists(['eyes', 'nose', 'lips', 'ears'], 'nose')
destruct_lists(['eyes', 'nose', 'lips', 'ears'], 'eyes')
destruct_lists(['eyes', 'nose', 'lips', 'ears'], 'ears')
