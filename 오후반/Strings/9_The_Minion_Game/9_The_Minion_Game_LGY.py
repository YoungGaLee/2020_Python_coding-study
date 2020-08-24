def minion_game(string):
    string = list(string)
    kevin = 0
    stuart = 0
    count = 0
    re = len(string)
    while(string != []):    
        count = 0
        for i in range(len(string)):
            s = string[:i+1]
            count += 1
        a = string.pop(0)
        
    
        if a in ['A','E','I','O','U'] :
            kevin += count
        else:
            stuart += count
        
    
    if kevin == stuart:
        print("Draw")

    elif kevin > stuart:
        print("Kevin", kevin)

    else:
        print("Stuart", stuart)


if __name__ == '__main__':
