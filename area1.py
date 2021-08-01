print("Enter the value of x1")
x1=int(input())
print("enter the value of x2")
x2=int(input())
print("enter the value of y1")
y1=int(input())
print("enter the value y2")
y2=int(input())
if x1>x2 and y1<y2:
	a=x1-x2;
	b=y2-y1
else:
	a=x2-x1;
	b=y1-y2

area=a*b
print("area is :")
print (area)