s=input()
k=int(input())
dict = {}
maximum = -1
i, j = 0, 0
while (j < len(s)):
    if (s[j] in dict):
        dict[s[j]] += 1
    elif (s[j] not in dict):
        dict[s[j]] = 1
    if (len(dict) == k):
        maximum = max(maximum, j - i + 1)
    elif (len(dict) > k):
        while (len(dict) > k):
            dict[s[i]] -= 1
            if (dict[s[i]] == 0):
                dict.pop(s[i])
            i = i + 1
    j = j + 1

print(maximum)
