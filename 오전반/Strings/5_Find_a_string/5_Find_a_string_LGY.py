def count_substring(sentence, finder):
    F = len(finder)
    count = 0
   
    for i in range(len(sentence)-2):
        if sentence[i:i+F] == finder:
            count += 1 
    return count

