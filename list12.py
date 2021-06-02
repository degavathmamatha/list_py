m=30
n=[10,11,12,13,14,17,18]
i=0
while i<len(n):
    j=i
    while j<len(n):
        if n[i]+n[j]==m:
            print(n[i],n[j],end='\n')
        j=j+1
    i=i+1
    #total sum