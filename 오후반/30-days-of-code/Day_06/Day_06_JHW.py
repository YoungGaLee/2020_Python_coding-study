# Enter your code here. Read input from STDIN. Print output to STDOUT
class Joo:
    def __init__(self,string):
        self.string=string
        self.length=len(self.string)
    def indexing(self):
        even=""
        odd=""
        for j in range(self.length):
            if j%2==0:
                even+=self.string[j]
            if j%2==1:
                odd+=self.string[j]
        print(even,odd)

t=int(input())
for i in range(0,t):
    a=str(input())
    p=Joo(a)
    p.indexing()
