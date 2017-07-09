def GetShortName(name):
  return name[0].upper()
  
def GetFullName(name):
  name = name.lower()
  return name[0].upper() + name[1:]

t = input()
for _ in xrange(t):
  names = map(str,raw_input().split())
  l = len(names)
  final = ''
  for i in xrange(l):
    if i == l-1:
      final +=  ' ' + GetFullName(names[i])
    else:
      final += ' ' + GetShortName(names[i]) + '.'
  print final.strip()
  