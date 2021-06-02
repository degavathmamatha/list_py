numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
print(len(numbers))
length=(len(numbers))
count=0
while (count<length):
    if (count>20) or (count<40):
        print(numbers[count])
        count=count+1