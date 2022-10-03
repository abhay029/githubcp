a1=int(input("number of rows for m 1: "))
b1=int(input("number of rows for m 1: "))
m1=[]
for i in range(a1):
    t=[]
    for j in range(b1):
        t.append(int(input()))
    m1.append(t)
    
a2=int(input("number of rows for m 2: "))
b2=int(input("number of cols in m 2: "))
m2=[]
for i in range(a2):
    t=[]
    for j in range(b2):
        t.append(int(input()))
    m2.append(t)
def matmul():
    m3=[[0 for i in range(len(m2[0]))] for j in range(len(m2))]
    for i in range(len(m1)):
        for j in range(len(m1[1])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k]*m2[k][j]


    for i in range(len(m2)):
        for j in range(len(m2[1])):
            print(m3[i][j],end=" ")
        print()





"""c1=[]
for i in range(len(a1)):
    for j in range(len(b1)):
        c1 = a1[i]+b1[j]

for i in c1:
    print(i,end=" ")"""