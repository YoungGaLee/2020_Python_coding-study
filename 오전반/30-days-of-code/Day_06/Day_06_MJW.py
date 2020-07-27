n = int(input())

for _ in range(n):
    input_str = input()
    output_str = input_str[::2] + ' ' + input_str[1::2]
    print(output_str)