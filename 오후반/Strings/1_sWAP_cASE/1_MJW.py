def swap_case(s):
    output_s = ''

    for x in s:
        output_s += x.lower() if x.isupper() else x.upper()
    return output_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)