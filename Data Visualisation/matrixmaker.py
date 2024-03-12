class matrix:
    def __init__(self,arr):
        self.arr
    def validity(self,m,n):
        return len(self.arr)==m*n
    def create_matrix(self,m,n):
        self.m=[]
        pass
    def disp_matrix(self):
        for i in self.m:
            print(*i)
lst=list(map(int,input().split()))
row,column=list(map(int,input().split()))   
m=matrix(lst)
if m.validity(row,column):
    m.create_matrix(row,column)
    m.disp_matrix()
else:
    print("invalid Dimension")