class Solution:
    
    def average(self, salary: List[int]) -> float:
        minsalary=float("inf")
        maxsalary=float("-inf")
        j=0

        for i in salary:
            if i<minsalary:
                minsalary=i
            if i>maxsalary:
                maxsalary=i
        salary.remove(maxsalary)
        salary.remove(minsalary)

        for i in salary:
            j+=i
        average=j/len(salary)

        return average
