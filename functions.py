def filter_even(number_list):
	result_list=[]
	for number in number_list:
		if number %2 ==0:
			result_list.append(number)
	return result_list

filter_even([1, 2, 3, 4, 5, 6, 7])


