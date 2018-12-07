def main():
    n = input()
    boxes = []
    for _ in xrange(n):
        a,b,c = map(int,raw_input().split())
        boxes.append([a*b,c,a,b])
        boxes.append([c*b,a,c,b])
        boxes.append([a*c,b,a,c])
    
    boxes = sorted(boxes, key = lambda x: x[0], reverse = True)
    print boxes
    stack = boxes[:1]
    total = stack[0][1]
    for i in xrange(1,len(boxes)):
        b1 = boxes[i][1]
        b2 = boxes[i][2]
        s1 = stack[-1][1] 
        s2 = stack[-1][2]
        if max(b1,b2) > max(s1,s2) and min(b1,b2) > min(s1,s2):
            stack.append(boxes[i])
            total += boxes[i][1]
        else:
            i-=1
    print stack
    print total
    
if __name__ == '__main__':
    main()