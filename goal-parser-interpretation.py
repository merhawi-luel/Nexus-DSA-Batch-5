class Solution:
    def interpret(self, command: str) -> str:
        i=0
        arr=[]
        while i < len(command):
            if command [i]=="G":
                arr.append("G")
                i+=1
            elif  command[i:i+2]=="()":
                arr.append("o")
                i+=2
            else:
                arr.append("al")
                i+=4
        return "".join(arr)

