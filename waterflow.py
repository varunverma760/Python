print("Enter the value of water level")
l=float(input())
if(l<30):
	print("low")
elif 30<l and l<=50:
	print("med")
elif 50<l:
	print("high")
else:
	print("Enter correct value of water level")