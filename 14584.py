import sys

sentence = sys.stdin.readline()
sentence = ''.join( x for x in sentence if x not in '\n')
n = int(sys.stdin.readline())
dictionary = []

for _ in range(n):
  q = sys.stdin.readline()
  q = ''.join( x for x in q if x not in '\n')
  dictionary.append(q)

while True:
  brk = False
  for i in dictionary:
    if sentence.find(i) != -1:
      print(sentence)
      brk = True
      break
  if brk:
    break

  arr = []
  for i in sentence:
    r = ord(i)+1
    if r == 123:
      r = 97
    arr.append(chr(r))
  sentence = ''.join(arr)