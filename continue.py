i=1
result =1
while i<20:
	i+=1
	if i%2==0:
		print("skipping {}".format(i))
		continue
	print("Multiplying with{}".format((i)))
	result=result*i
result('i:', i)
print('result:',result)
