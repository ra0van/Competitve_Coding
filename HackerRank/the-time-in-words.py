# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/the-time-in-words

h = int(raw_input())
m = int(raw_input())
arr = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','thirty','fourty','fourty one','fourty two','fourty three','fourty four','fourty four','fourty five','fourty six','fourty seven','fourty eight','fourty nine','fifty','fifty one','fifty two','fifty three','fifty four','fifty five','fifty six','fifty seven','fifty eight','fifty nine','sixty']
if m == 0:
    print arr[h-1],
    print "o' clock"
elif m==60:
    if h==12:
        h = 1
    print arr[h-1],
    print "o' clock"
elif m>=1 and m<=29 and m!=15:
    mins = ''
    if m == 1:
        mins += "minute"
    else:
        mins += "minutes"
    print arr[m-1],mins,'past',arr[h-1]
elif m==15:
    print "quarter past",arr[h-1]
elif m==30:
    print "half past "+arr[h-1]
elif m>=31 and m<=59 and m!=45:
    if h ==12:
        h = 1
    else:
        h += 1
    mins = ''
    if m-59 == 1:
        mins += "minute"
    else:
        mins += "minutes"
    print arr[59-m],mins,"to",arr[h-1]
elif m==45:
    if h ==12:
        h = 1
    else:
        h += 1
    print  "quarter to",arr[h-1]