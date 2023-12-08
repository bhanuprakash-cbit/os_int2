n=int(input("Enter the number of files:"))
sb=[]
s=[]
m=[]
b=[]
for i in range(n):
    print("enter the starting block and size of file",i+1,":",end="")
    sb_i,s_i=map(int,input().split())
    sb.append(sb_i)
    s.append(s_i)
    print("enter the blocks occupied by file",i+1,":",end="")
    m_i=int(input())
    m.append(m_i)
    print("Enter blocks of file",i+1,":",end="")
    b_i=list(map(int,input().split()))
    b.append(b_i)
print("Filename\tIndex\tLength")
for i in range(n):
    print(i+1,"\t",sb[i],"\t",m[i])
x=int(input("Enter the file name: "))
print("file name is ",x)
print("Index is ",sb[x-1])
print("blocks occupied are : ",end="")
for j in range(m[x-1]):
    print("%3d" % b[i][j], end="")