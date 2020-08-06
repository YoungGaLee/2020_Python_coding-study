def swap_case(S):
    total = ""
    for s in S:
        if s.isupper() == 1 :
            total += s.lower()
        else:
            total += s.upper()
    return total

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
