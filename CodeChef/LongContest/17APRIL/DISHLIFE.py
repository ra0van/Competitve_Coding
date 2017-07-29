t = input()
for i in range(t):
    n,k = map(int,raw_input().split())
    #print n,k
    islands = []
    visited = [0]*k
    visited_count = 0
    for j in range(n):
        ingredient = map(int,raw_input().split())
        ingredient = ingredient[1:]
        islands.append(ingredient)
    #print islands
    for ingredient in islands:
        needed = False
        if sum(ingredient) == k*(k+1)/2:
            visited_count+=1
            visited = [1]*k
            break
        for spice in ingredient:
            if visited[spice-1]==0:
                visited[spice-1]=1
                needed = True
        if needed:
            visited_count +=1
    #print visited
    if sum(visited) == k:
        if visited_count <n:
            print 'some'
        else:
            print 'all'
    else:
        print 'sad'
 
