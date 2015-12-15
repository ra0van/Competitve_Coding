
while True:
	a,d = map(int,raw_input().split())
	if a==0 and d==0:
		break
	att = map(int,raw_input().split())
	defe = map(int,raw_input().split())

	att_min = min(att)
	def_min = min(defe)
	defe.remove(def_min)
	def_sec_min = min(defe)
	if def_sec_min > att_min:
		print "Y"
	else:
		print "N"


