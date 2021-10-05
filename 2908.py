a, b = map(str, input().split())

a = ''.join(reversed(a))
b = ''.join(reversed(b))
print(max(a,b))