class array:
    def __init__(self,lst,r=0,c=0):
        self.lst=lst
        self.r=r
        self.c=c
        if r!=0 and c!=0:
            M=[]
            tmp=[]
            for i in self.lst:
                tmp.append(i)
                if len(tmp)==c:
                    M.append(tmp)
                    tmp=[]
        self.lst=M        
    def __add__(self,other):
        if (self.r,self.c)==(other.r,other.c):
            M=eval(str([[0]*self.c]*self.r))
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j]=self.lst[i][j]+other.lst[i][j]
            return array(M)        
        else:
            print("Dimension is not valid")

    def disp_mat(self):
        for i in self.lst:
            print(*i)



#Driveer code 
    
lst1=list(map(eval,input().split()))
r1,c1=list(map(eval,input().split()))
arr1=array(lst1,r1,c1)


lst2=list(map(eval,input().split()))
r2,c2=list(map(eval,input().split()))
arr2=array(lst2,r2,c2)

print("\nMatrix 1")
arr1.disp_mat()


print("\nMatrix 2")
arr2.disp_mat()


out=arr1 + arr2
out.disp_mat()

print("\nAddition")
out.disp_mat()


