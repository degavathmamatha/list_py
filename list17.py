elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
count_even = 0
count_odd = 0
sum_even=0
sum_odd=0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		count_even= count_even +1
		sum_even= sum_even + elements[i]
		avg_even= sum_even/4
	else: 
		count_odd = count_odd +1
		sum_odd= sum_odd + elements[i]
		avg_odd= sum_odd/7
	i= i+1
print("Even numbers in the list: ", count_even,"sum of even=",sum_even,"avrg of even:",avg_even)
print("Odd numbers in the list: ", count_odd,"sum of odd=",sum_odd,"avrg of odd:",avg_odd)
# sab sath sath mein