lis=[1,2,3]
for i in lis:
      print(i)#0,1,2,3


lis=[10,20,30,40]
print((10*2)in lis)#20 in list so true
print(lis[1]+lis[-1])#1=20 2=40 so "20+40"=60


lis=[1,2,3]
print(len(lis))#count list
print(min(lis))#lowest no list
print(max(lis))#higest no list


#type
lis=[1,2,3,4,5]
lis.append(1)#add with [no]
print(lis)
lis.insert(4,2)#add 4 index on 2
print(lis)
lis.remove(3)#remove 3 one of a number
print(lis)
lis.extend([6,7,8,9])#add no on with out []
print(lis)
lis.pop(0)#remove index on "0"
print(lis)
element=lis.pop(2)
print(element)#store .pop
 
lis.sort()#assending order
print(lis)
 
lis.sort(reverse=True)#desending order
print(lis)

LIST=list("dhanabal")#split element
print(LIST)



