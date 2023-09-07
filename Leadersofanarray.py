A=list(map(int,input().split()))
N=len(A)
maxright = A[N - 1]
leaders = [maxright]
for i in range(N - 2, -1, -1):
    if (A[i] >= maxright):
        maxright = A[i]
        leaders.append(maxright)
leaders.reverse()
print(*leaders)