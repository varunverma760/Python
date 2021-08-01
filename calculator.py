#python code for calculator
choice=int(input("Enter your choice"))
print("Enter two numbers")
a=int(input())
b=int(input())

if choice == 1:
	res=a+b
	print("Result = ",res)
elif choice == 2:
	res=a-b
	print("Result = ",res)
elif choice == 3:
	res=a*b
	print("Result = ",res)
elif choice == 4:
	res=a/b
	print("Result = ",res)
elif choice == 5:
	res=a%b
	print("Result = ",res)
elif choice == 6:
	exit()
else:
	print("INVALID OPERATION")
