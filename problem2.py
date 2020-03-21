while True:
  seq = input('ENTER THE SEQUENCE:')
  no_of_G = 0
  no_of_C = 0
  GC_Percent = 0
  for i in seq:
    if i == 'G':
      no_of_G += 1
    elif i == 'C':
      no_of_C += 1
  GC_Percent = (no_of_G + no_of_C) * 100 / len(seq)
  print(GC_Percent)
  num = input('IF YOU WANT TO CHECK FOR ANOTHER SEQUENCE PRESS 1 ELSE 0')
  if num == '0':
    break
