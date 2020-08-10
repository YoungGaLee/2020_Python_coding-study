def swap_case(s):
    S = s
    result= []
    for i in range(len(S)):
        if S[i] == S[i].lower():
            result.append(S[i].upper())

        else :
            result.append(S[i].lower())

    result =''.join(result)
    return result
    
'''
def swap_case(s):
    return (s.swapcase())
'''

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
