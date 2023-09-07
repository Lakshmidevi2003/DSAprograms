def stringCount(n: int, s: str) -> int:
    # Write your code here.
    str = ''
    i = 0
    j = 0
    count = 0
    while (j < n):
        str = str + s[j]
        if (j - i + 1 == 2):
            if (str == "#*" or str == "*#"):
                count += 1
            str = str[1:]
            i += 1
        j += 1
    return count
    pass


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        result = stringCount(n, s)
        print(result)




