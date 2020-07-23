n = int(input())

phone_book = dict()

for _ in range(n):
    x = input().split(' ')
    name, phone_number = x[0], x[1]
    phone_book[name] = phone_number

for _ in range(n):
    query_name = input()
    if query_name in phone_book:
        phone_number = phone_book[query_name]
        print('{}={}'.format(query_name, phone_number))
    else:
        print('Not found')

    