def mutate_string(string, position, character):
    S  = list(string)
    S[position] = character
    return ''.join(S)
 
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
