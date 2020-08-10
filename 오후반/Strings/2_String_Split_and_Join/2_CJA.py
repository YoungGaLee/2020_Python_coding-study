def split_and_join(line):
    #함수X
    a = ''
    for i in range(len(line)):
        if line[i] != ' ':
            a += line[i]
        else :
            a += '-'

    #함수O
    #a = '-'.join(line.split())
    
    return(a)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
