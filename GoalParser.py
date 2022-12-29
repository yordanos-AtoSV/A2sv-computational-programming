class Solution:
    def interpret(self, command: str) -> str:
        answer=[]
        j=""
        for i in range(len(command)):
            if command[i]=="G":
                answer.append(command[i])
            elif command[i]=="(":
                if command[i+1]==")":
                    answer.append("o")
                else:
                    answer.append("al")

                
        for i in range(len(answer)):
            j+=answer[i]
    

        return j  
