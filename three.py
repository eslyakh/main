
number = int(input('Введите кол-во процентов:'))

if number == 1 or number == 21 or number == 31 or number == 41 or number == 51 or number == 61 or number == 71 or number == 81 or number == 91:
  print(number, 'процент')
elif number >= 2 and number <= 4 or number >= 22 and number <= 24 or number >= 32 and number <= 34 or number >= 42 and number <= 44 or number >= 52 and number <= 54 or number >= 62 and number <= 64 or number >= 72 and number <= 74 or number >= 82 and number <= 84 or number >= 92 and number <= 94:
  print(number, 'процента')
else:
  print(number, 'процентов')