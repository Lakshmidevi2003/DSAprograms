arr = list(map(int, input().split()))
n = len(arr)


def insertionsort(arr, n):
    for i in range(1, n):
        anchor = arr[i]
        j = i - 1
        while (j >= 0 and anchor < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = anchor
    return arr
print(insertionsort(arr, n))
