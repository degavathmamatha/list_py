num=30
n=[10,11,12,13,14,17,18,19]

i=0
b=[]
while i<len(n):
	j=i
	a=[]
	while j<len(n):
		if n[i] + n[j] ==num:
			a.append(n[i])
			a.append(n[j])
			b.append(a)
		j=j+1
	i=i+1
print(b)

##output is [[11,19],[12,18],[13,17]]