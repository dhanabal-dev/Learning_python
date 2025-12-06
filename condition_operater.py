a=10
if(a<1 and a<2):
   print("true")
elif(a<11 and a<12):
   print("a is smalest no")
else:
   print("false")
#2
a=int(input())
if(a%3==0 and a%5==0):
   print("3 and 5 divided")
else:
   print("3 and 5 is not divided")
#MINI CALCULATER
a=int(input())
b=int(input())
cal=input("add/sub/mult/div")
if(cal=="add"):
   print(a+b)
elif(cal=="sub"):
   print(a-b)
elif(cal=="mult"):
   print(a*b)
elif(cal=="div"):
   print(a/b)
else:
   print("hi")