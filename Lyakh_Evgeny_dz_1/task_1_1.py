
duration = int(input('Введите продолжительность секунд: '))

s = duration < 60
m = duration < 3600 and duration >= 60
h = duration < 86400 and duration >= 3600
d = duration >= 86400

if s == True:
  print(duration, 'сек')
  
elif m == True:
  print(duration // 60, 'мин', duration % 60, 'сек')
  
elif h == True:
  print(duration // 3600, 'час', (duration % 3600) // 60, 'мин', duration % 60, 'сек')
  
else:
  print(duration // 86400, 'дн', (duration % 86400) // 3600, 'час', (duration % 3600) // 60, 'мин', duration % 60, 'сек')