import math
import sys

t = int(input())

for i in range(t):
  a, b = [int(x) for x in input().split()]
  n = int(input())
  for j in range(n):
    guessed_num = math.ceil((a + b) / 2)
    print(guessed_num)
    sys.stdout.flush()
    result = input()
    if result == 'CORRECT':
      break
    elif result == 'TOO_SMALL':
      a = guessed_num
    elif result == 'TOO_BIG':
      b = guessed_num - 1
    else:
      raise Exception('Unknown result: %s' % result)
