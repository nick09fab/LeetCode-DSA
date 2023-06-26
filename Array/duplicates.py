lst = [1,1,2,2,3,4]

def remove_duplicates(arr):
    de_duped_list = []
    for val in arr:
        if val not in de_duped_list:
            de_duped_list.append(val)
    return de_duped_list

print(remove_duplicates(lst))

