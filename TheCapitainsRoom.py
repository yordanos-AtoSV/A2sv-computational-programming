def TheCapitainsRoom():
    n = int(input())
    l = list(input().split())
    a = set()
    b = set()
    for i in l:
        if i not in a:
            a.add(i)
            b.add(i)
        else :
            b.discard(i)
    b=list(b)
    print(b[0])
    
    
TheCapitainsRoom()
