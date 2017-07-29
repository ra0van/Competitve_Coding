#https://www.codechef.com/problems/COOK82A
t = input()
barca = 'Barcelona'
real = 'RealMadrid'
eibar = 'Eibar'
malaga = 'Malaga'
for _ in xrange(t):
  barca_score = 0
  real_score = 0
  eibar_score = 0
  malaga_score = 0
  
  for _ in xrange(4):
    t,s = map(str,raw_input().split())
    if t==barca:
      barca_score = int(s)
    elif t==real:
      real_score = int(s)
    elif t==eibar:
      eibar_score = int(s)
    elif t==malaga:
      malaga_score = int(s)
  
  if(real_score<malaga_score) and (barca_score>eibar_score):
    print barca
  else:
    print real
  
