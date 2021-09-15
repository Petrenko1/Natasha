lines=[1,7,9,15,8,4,5]
Smax=0
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        for k in range(j+1,len(lines)):
            a=lines[i]
            b=lines[j]
            c=lines[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                S=(p*(p-a)*(p-b)*(p-c))**0.5
                if S>Smax:
                    Smax=S
print(Smax)
