class Solution:
    def calculateD(self, x1:int, y1:int, x2:int, y2:int):

        dest=abs(x1 - x2) + abs(y1 - y2)
        return dest

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minD=float("inf")
        index=-1
        

        for i in range(len(points)):
           newx=points[i][0]
           newy=points[i][1]

           if x==newx or y==newy:
               currentD=self.calculateD(x,y,newx,newy)
               if currentD<minD:
                   minD=currentD
                   index=i
        return index
