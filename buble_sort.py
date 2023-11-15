def b_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [2,14,6,4,3,3,15,3,18,8]
print(b_sort(arr))

def dhcbhsj():
    vdjf v  kjsvnskj
