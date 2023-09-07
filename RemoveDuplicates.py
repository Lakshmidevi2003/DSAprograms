arr= list(map(int, input().split()))
arr.sort()
def remove_duplicates(arr):
    n = len(arr)
    if n == 0:
        return 0

    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return arr[:i+1]

result=remove_duplicates(arr)
print(result)
