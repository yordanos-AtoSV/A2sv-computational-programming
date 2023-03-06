

    size = int(input())
    queue = list(map(str, input().split()))
    case = int(input())
    for i in range(case):
        word = input()
      
        for j in range(len(queue)):
          
            if word < queue[j]:
      
                print(j)
         
                break
            if j == len(queue) - 1:
               
                print(len(queue))
                break
