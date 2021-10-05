string = input()
result = ""

for i in range(len(string)):
  if ord(string[i-1]) >=65 and ord(string[i-1]) <= 90:
    result +=string[i-1]

print(result)