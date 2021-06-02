marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
sum=0
while i<len(marks[0]):
    sum=sum+marks[0][i]+marks[1][i]+marks[2][i]
    i=i+1
print(sum)