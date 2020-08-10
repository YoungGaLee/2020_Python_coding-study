def count_substring(string, sub_string):
    count = 0
    A,B = len(string),len(sub_string)
    
    for i in range(A-B+1):
        if string[i:i+B] == sub_string:
            count += 1
        else:
            pass
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
