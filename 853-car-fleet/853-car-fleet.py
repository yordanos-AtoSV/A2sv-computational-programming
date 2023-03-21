class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [0] * len(position)
        for i in range(len(position)):
            cars[i] = [position[i],speed[i]]
            
            
        cars.sort(reverse = True)
        stack = []
        for c in cars:
            stack.append((target - c[0]) / c[1]) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
        
#         check = []
#         for c in cars:
            
#             check.append((target - c[0]) // c[1])
        
#         stack = []
#         count = 0
#         flag = 1
#         for c in check:
#             if len(stack) != 0:
#                 if c < stack[-1]:
#                     stack.pop()
#                     count += 1
#                     flag = 0
#                 else:
                    
#                     while len(stack) != 0:
#                         stack.pop()
                        
#                     count += 1
#                     continue
                        
#             stack.append(c)
                
#         if flag == 1:
#             return 1
#         return count
        