#print row
def row(n):
  if (n == 0):
    return
  print ('*', end = ' ')

  #calling row using recursion
  row(n- 1)

#create the pattern
def pattern(n, i):
  if (n == 0):
    return
  row(i)
  print('\n', end = ' ')

  #using recursion to display astericks
  pattern(n - 1, i + 1)

def main():
  n = int(input('How many lines to display: '))
  pattern(n, 1)

  input("Press the <Enter> to quit")

main()
