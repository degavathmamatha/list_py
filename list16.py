elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
sum_even = 0
sum_odd = 0
i = 0 
while(i < len(elements)):
	if elements[i] % 2 ==0:
		sum_even= sum_even + elements[i]
		avg_even= sum_even/4
	else: 
		sum_odd= sum_odd + elements[i]
		avg_odd= sum_odd/7
	i= i+1
print(avg_even)
print(avg_odd)
# avg of even and odd