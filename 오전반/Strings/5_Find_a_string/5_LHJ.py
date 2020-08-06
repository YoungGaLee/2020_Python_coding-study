def count_substring(string, sub_string):
    idx = 0
    n = 0
    while idx != -1:
        idx = string.find(sub_string, idx)
        if idx != -1:
            n+=1
            idx += 1
    return n
