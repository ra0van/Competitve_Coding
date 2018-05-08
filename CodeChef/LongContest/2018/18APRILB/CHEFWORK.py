import sys
n = input()
cost = map(int,raw_input().split())
type = map(int,raw_input().split())

type_cost = {}

for i in xrange(1,4):
	type_cost[i] = [] 

for i in xrange(n):
	type_cost[type[i]].append(cost[i])

# print type_cost


auth_cost = sys.maxint
if len(type_cost[2])>0:
	auth_cost = min(type_cost[2])
	
auto_cost = sys.maxint
if len(type_cost[3])>0:
	auto_cost = min(type_cost[3])
	
	
trans_cost = sys.maxint
if len(type_cost[1])>0:
	trans_cost = min(type_cost[1])
	
trans_cost = min(trans_cost,auto_cost)

print min(auto_cost,trans_cost+auth_cost)