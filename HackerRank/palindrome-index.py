# Enter your code here. Read input from STDIN. Print output to STDOUT
# partial 40/50

def isPalin(l):
    l = ''.join(l)
    if l[::-1] == l:
        return True

t = int(raw_input())
for i in range(t):
    word = raw_input()
    l = list(word)
    if isPalin(l):
        print -1
    else:
        for i in range(len(l)):
            tmp = l[:i]+l[i+1:]
            if isPalin(tmp):
                print i
                break;
         