arr = [2,4,3,5,6,-2,4,7,8,9]

def pair_sum(arr, sum):
    pair_sum_list = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                pair_sum_list.append(f"{arr[i]} + {arr[j]}")

    return pair_sum_list

print(pair_sum(arr,7)
)