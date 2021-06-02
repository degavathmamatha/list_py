row=int(input("en"))
c=int(input("en"))
i=1
a=1
list1=[]
while i<=row:
	b=a
	j=1
	list2=[]
	while j<=c:
		list2.append(b)
		j=j+1
		b=b+1
	list1.append(list2)
	i=i+1
	a=a+c
print(list1)

#logic in row and coloum