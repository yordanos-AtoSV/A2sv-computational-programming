def lessEqual():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    temp = array[k -1]
    count = 0 
    if k == 0:
        if array[0] > 1:
            print(array[0] - 1 )
        else:
            print( "-1" )
        return 0
    
    for i in range (n):
        if array[i] <= temp:
            count += 1
    if count == k:
      
        print( temp)
    else:
        print( "-1" )
lessEqual()
