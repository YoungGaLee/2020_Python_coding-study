def print_full_name(first_name, last_name):
 a = "Hello %s %s! You just delved into python." %(first_name, last_name)
 return a
print (a)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
