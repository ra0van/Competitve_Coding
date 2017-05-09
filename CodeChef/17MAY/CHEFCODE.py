# partially correct 
'''
Sub-Task	Task #	Score	Result
(time)
1	6	NA	AC
(0.000000)
1	7	NA	AC
(0.000000)
1	9	NA	AC
(0.010000)
Final Score - 30.000000	Result - AC
2	0	NA	WA
(0.140000)
2	1	NA	TLE
(5.010000)
2	2	NA	AC
(0.000000)
2	3	NA	WA
(0.360000)
2	4	NA	WA
(2.240000)
2	5	NA	AC
(0.000000)
2	8	NA	TLE
(5.010000)
2	10	NA	AC
(0.010000)
Final Score - 0.000000	Result - WA
'''
def calculate(curr,unused,p):
  global sup
  global k
  if len(unused) == 0:
    return
  if p>k:
    return
  for i in unused:
    new = list(curr)
    new.append(i)
    new.sort()
    v = p*i
    if v <= k:
      rem = list(unused)
      rem.remove(i)
      if new not in sup:
        sup.append(new)
        calculate(new,rem,v)
  
 
n,k = map(int,raw_input().split())
s = map(int,raw_input().split())
sup = [s]
calculate([],s,1)
count = 0
for s in sup:
  prod = 1
  for i in s:
    prod *= i
    if prod>k:
      count += 1
      break
print len(sup)-count
