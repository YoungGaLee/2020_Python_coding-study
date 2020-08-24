def minion_game(string):
    vowels = 'AEIOU'
    len_str = len(string)

    Stuart, Kevin = 0, 0
    for i in range(len(string)):
        if not string[i] in vowels:
            Stuart += len_str - i
        else:
            Kevin += len_str - i

    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Stuart < Kevin:
        print('Kevin', Kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)