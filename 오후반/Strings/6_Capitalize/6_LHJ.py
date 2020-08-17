def solve(s):
    re = ""
    flag = True
    for x in s:
        if flag:
            if x.isalpha():
                re += x.upper()
                flag = False
            elif x.isalnum():
                re += x
                flag = False
            else: re += x
        else:
            if x.isspace():
                flag = True
            re += x
    
    return re
