#돌연변이, 변화

def mutate_string(string, position, character):
    list_string = list(string)

    list_string[position] = character
    
    ans = ''.join(list_string)
    return ans

# S는 문자열, i, c도 문자열 position은 정수형.
