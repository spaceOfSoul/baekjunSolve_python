n = input()

caps = n.upper()
dictionary = {}
for i in caps:
  if i in dictionary.keys():
    dictionary[i] += 1
  else:
    dictionary[i] = 1

a = max(dictionary.values())

count = 0
result = ''
for i in dictionary.items():
  if i[1] == a:
    count += 1
    result = i[0]
  if count == 2:
    print('?')
    break
if count == 1:
  print(result)