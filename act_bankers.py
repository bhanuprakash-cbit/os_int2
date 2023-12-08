p=int(input("Enter the number of processes: "))
r=int(input("Enter the number of resources:"))
print("Enter the allocated matrix: ")
alloc=[]
for i in range(p):
    l=list(map(int,input().strip().split()))
    alloc.append(l)
print("Enter the maximum matrix:")
max=[]
for i in range(p):
    l=list(map(int,input().strip().split()))
    max.append(l)
print("Enter the available matrix: ")
avail=list(map(int,input().strip().split()))
print("Allocated Matrix: ",alloc,end="\n")
print("Max Matrix: ",max,end="\n")
print("Available Matrix: ",avail,end="\n")
finish=[0]*p
safeseq=[0]*p
count=0
for i in range(p):
    finish[i]=0
need=[[0 for i in range(r)] for i in range(p)]
for i in range(p):
    for j in range(r):
        need[i][j]=max[i][j]-alloc[i][j]
x=0
for k in range(p):
    for i in range(p):
        if (finish[i]==0):
            flag=0
            for j in range(r):
                if (need[i][j]>avail[j]):
                    flag=1
                    break
            if (flag==0):
                safeseq[count]=i
                count+=1
                for x in range(r):
                    avail[x]+=alloc[i][x]
                finish[i]=1
                
print("safe sequence:")
for i in range(p-1):
    print("p",safeseq[i],"->",sep="",end="")
print("p",safeseq[p-1],sep="")