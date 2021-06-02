places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
i=1
while i<=len(places):
	print(places[-i],end=' ')
	i=i+1
	#reverse string without using function and slicing
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 

i=1
j=[]
while i<=len(places):
	j.append(places[-i])
	i=i+1
print(j)
	#list ke ander list