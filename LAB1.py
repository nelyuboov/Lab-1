import random
with open("books.csv") as f:
    a=f.readlines()
print(len(a))
k=0
for i in range(len(a)):
    q=a[i].split(';')
    if len(q[1])>30:
        k+=1
print(k)
vv=str(input())
for i in range(len(a)):
    q=a[i].split(';')
    if q[3]==vv:
        print(a[i])
        
s=[random.randint(0,len(a)) for i in range(20)]
myfile=open('bf.txt',"w+")
m=1
for i in s:
    q=a[i].split(';')
    l=q[3]+'. '+ q[1] +' - '+ q[6]
    myfile.write(str(m)+') '+l+"\n")
    m+=1
myfile.close()
