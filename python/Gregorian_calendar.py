while True:
  value = input('year [q to quit]: ')

  if value == 'q':
    break
  numbar = int(value)
  t1 = numbar/4
  if t1 == int(t1):
    t2 = numbar/100
    if t2 == int(t2):
      t3 = numbar/400
      if t3 == int(t3):
        print('{} is a leap year'.format(numbar))
      else:
        print('{} is not a leap year'.format(numbar))
    else:
      print('{} is a leap year'.format(numbar))
  else:
    print('{} is not a leap year'.format(numbar))
