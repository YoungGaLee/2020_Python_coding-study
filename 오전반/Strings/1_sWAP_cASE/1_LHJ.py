def swap_case(s):
    a = s[:]
    a = a.upper()
    s = list(s)

    for i in range(len(s)):
        if s[i] == a[i]:
            s[i]=s[i].lower()
        else:
            s[i]=s[i].upper()
            
    return "".join(s)
