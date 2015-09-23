#https://www.hackerearth.com/tarams-python-developer-hiring-challenge/algorithm/marut-vs-devil-in-hunger-games-1/
#All passed
# Time : 4.4002s
def getScore(pos1,pos2,i,alpha):
	if pos1==0:
		return 0
	elif pos1-pos2>0:
		return (pos1-pos2)*(alpha[i])
	return 0


alpha = map(int,raw_input().split())

q = int(raw_input())
fcM = 0
fcD = 0
for i in range(q):
	
	m = raw_input()
	d = raw_input()
	
	finalM = [0]*26
	finalD = [0]*26
	
	countM = 0
	countD = 0
	
	for i in range(26):
		ch = chr(i+97)
		tmp1 = m.count(ch)
		tmp2 = d.count(ch)
		
		countM += getScore(tmp1,tmp2,i,alpha)
		countD += getScore(tmp2,tmp1,i,alpha)
		
	
	fcM += countM
	fcD += countD
	
if fcM > fcD:
	print "Marut"
elif fcM < fcD:
	print "Devil"
else:
	print "Draw"
		
		
		
		