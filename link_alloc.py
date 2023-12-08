class file:
    def __init__(self):
        self.fname=""
        self.start=0
        self.size=0
        self.block=[]
n=int(input("Enter the number of files: "))
f=[file() for _ in range(n)]
for i in range(n):
    f[i].fname=input("Enter file name: ")
    f[i].start=int(input("Enter starting block: "))
    f[i].block.append(f[i].start)
    f[i].size=int(input("Enter number of blocks: "))
    for j in range(1,f[i].size+1):
        f[i].block.append(int(input()))
print("File\tstart\tsize\tblock")
for i in range(n):
    print(f"{f[i].fname}\t{f[i].start}\t{f[i].size}\t",end="")
    for j in range(1,f[i].size):
        print(f"{f[i].block[j]}-->",end="")
    print(f"{f[i].block[f[i].size]}")