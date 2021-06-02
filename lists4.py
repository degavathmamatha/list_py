# write a program for binary digit
binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=-1
a=0
sum=0
while i>=(-len(binary_number)):
    sum=sum+(binary_number[i]*2**a)
    a=a+1
    i=i-1
print(sum)
