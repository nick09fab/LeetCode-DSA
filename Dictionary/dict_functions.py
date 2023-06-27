"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
{'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""

def merge_dicts(dict1, dict2):
    # TODO
    merged_dict = dict1.copy()

    for key in dict2:
        if key not in merged_dict:
            merged_dict[key] = dict2[key]
        else:
            merged_dict[key] = merged_dict.get(key) + dict2[key]

    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dicts(dict1, dict2))


"""
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))

"""
def max_value_key(my_dict):
    # TODO
    max_value = max(my_dict.values())
    for key,value in my_dict.items():
        if value == max_value:
            return key

print(max_value_key( {'a': 5, 'b': 9, 'c': 2}))


def reverse_dict(my_dict):
    d = {}
    for key, val in my_dict.items():
        d[val] = key

    return d

print(reverse_dict( {'a': 1, 'b': 2, 'c': 3}))