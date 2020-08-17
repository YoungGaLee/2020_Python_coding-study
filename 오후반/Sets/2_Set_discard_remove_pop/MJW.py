n = int(input())
s = set(map(int, input().split()))

n_cmd = int(input())

for _ in range(n_cmd):
    cmd = input().split()

    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))

print(sum(s))
