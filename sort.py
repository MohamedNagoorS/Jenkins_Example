a=int(input())
b=(input().split(" "))
c=[]
e=[]
for i in range (a):
    c.append(int(b[i]))
    e.append(c[i])
asc=0
dsc=0
for i in range(a-1):
    for j in range(0, a-i-1):
 
        if c[j] > c[j + 1]:
            asc+=1
            c[j], c[j + 1] = c[j + 1], c[j]

for i in range(a-1):
    for j in range(0, a-i-1):
 
        if e[j] < e[j + 1]:
            dsc+=1
            e[j], e[j + 1] = e[j + 1], e[j]
print(asc)
print(dsc)
if(asc<dsc):
    print (asc)
else:
    print(dsc)
print("Hi")