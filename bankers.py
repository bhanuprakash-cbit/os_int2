# procs = int(input('Enter the number of processes: '))
# resrs = list(map(int, input('Enter the total resources of system: ').split()))

procs = 5
resrs = [10,5,7]

alloc = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_need = [[7,5,3],[3,2,2],[9,0,2],[4,2,2],[5,3,3]]

# alloc = []
# max_need = []

# print('Enter the allocated resources in matrix form: ')
# for i in range(procs):
#     temp = list(map(int, input().split()))
#     alloc.append(temp)

# print('Enter the max need of resources in matrix form: ')    
# for i in range(procs):
#     temp = list(map(int, input().split()))
#     max_need.append(temp)

avail = []
for i in range(len(resrs)):
    l = 0
    for j in range(procs):
        l += alloc[j][i]
    avail.append(l)

rem_need = []
for i in range(procs):
    temp = []
    for j in range(len(resrs)):
        a = max_need[i][j]-alloc[i][j]
        temp.append(a)
    rem_need.append(temp)

f = [0]*procs
ans = [0]*procs
ind = 0

for k in range(procs):
    f[k] = 0

for k in range(procs):
    for i in range(procs):
        if f[i] == 0:
            flag = 0
            for j in range(len(resrs)):
                if rem_need[i][j] > avail[j]:
                    flag = 1
                    break
            if flag == 0:
                ans[ind] = i
                ind += 1
                for y in range(len(resrs)):
                    avail[y] += alloc[i][y]   

print('Safe sequence')
for i in range(procs-1):
    print(f'P{ans[i]} ->')
