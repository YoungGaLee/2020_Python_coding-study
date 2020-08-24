def minion_game(string):
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i
    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Stuart > Kevin:
        print('Stuart', Stuart)
    else:
        print('Draw')


