#partially correct
t = input()
for i in range(t):
    n,k = map(int,raw_input().split())
    islands = []
    visited = [0]*k
    visited_count = 0
    first = False
    for j in range(n):
        needed = False
        ingredient = list(set(map(int,raw_input().split())))
        islands.append(ingredient)
        if j==0:
            if sum(visited) == k*(k+1)/2:
                first = True
                break
        for spice in ingredient:
            if visited[spice-1]==0:
                visited[spice-1]=1
                needed=True
        if needed:
            visited_count+=1
    if first:
        print 'some'
    elif sum(visited) != k:
        print 'sad'
    else:
        if visited_count ==n:
            print 'all'
        else:
            print 'some'
