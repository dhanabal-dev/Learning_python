
# for i in range(1,10):
#     print(i)
name=[10,20,30,40,50]
for i in name:
    if (i==90):
        break
else:
   print("else is exicuted")
for i in range(1,10):
    if(i==5):
        continue
else:
    print("wrong")
for i in range(1,11):
    print(i,"x2 =",i*2)
#NEW
a=8
b=15
for i in range(a+1,b):
    print(i)
#even no
for i in range(1,11):
    if(i%2==0):
       print(i)
#count
c=0
co=0
for i in range(1,11):
    if(i%2==0):
        c=c+1
    else:
        co=co+1
print(c)
print(co)


