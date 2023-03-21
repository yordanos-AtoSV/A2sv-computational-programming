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
        

        