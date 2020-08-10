def mutate_string(string, position, character):
    a=string[position]
    ans1=string[:position]
    ans2=string[position:]
    ans2=ans2[1:]
    ans2=character+ans2

    return ans1+ans2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
