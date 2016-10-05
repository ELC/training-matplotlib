def power(s):
    r = []
    for j in range(len(s)):
        for i in range(j,len(s)):
            r.append(s[j:i])
    print([i for i in r ])