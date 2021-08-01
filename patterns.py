print("Enter the value of n")
n=int(input())
i=1
while i<=n:
	j=1
	while j<=n:
		#print the jth column
		print('*',end='')
		j=j+1
	print()
	i=i+1
