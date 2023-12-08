n=int(input("Enter the number of files: "))
b=[0]*20
sb=[0]*20
t=[0]*20
c=[[0]*20 for _ in range(20)]
for i in range(n):
    b[i]=int(input("Enter the number of blocks occupied by file {} : ".format(i+1)))
    sb[i]=int(input("Enter the starting block of file {} : ".format(i+1)))
    t[i]=sb[i]
    for j in range(b[i]):
        c[i][j]=sb[i]
        sb[i]+=1
print("Filename\tStarting Block\tLength")
for i in range(n):
    print("{}\t\t{}\t\t{}".format(i+1,t[i],b[i]))
x=int(input("enter the file name: "))
print("File name is {} : ".format(x))
print("Length is {} : ".format(b[x-1]))
print("Blocks occupied is : ",end="")
for i in range(b[x-1]):
    print("{:4d}".format(c[x-1][i]),end="")
