def max_product(arr:list):
    """
    arr = [1,7,3,4,9,5]
    max_product[arr] = 9 * 7 = 63
    """
    max_value = max(arr) # get the max value from the array
    arr.remove(max_value)
    second_max_value = max(arr)

    return max_value * second_max_value

def max_product(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]

arr =  [1,7,3,4,9,5]
print(max_product(arr))

arr =  [1,7,3,4,9,5]
print(max_product(arr))