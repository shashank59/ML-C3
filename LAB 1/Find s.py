import csv
a=[]
with open('data.csv') as dataset:
    for x in csv.reader(dataset):
        a.append(x)
a.remove(a[0])
msh = ['0']*(len(a[0])-1)
for x in a:
    if x[len(x)-1]=='yes' or x[len(x)-1]=='Yes':
        for i in range(0,len(msh)):
            if msh[i]=='0' or msh[i]==x[i]:
                msh[i]=x[i]
            else:
                msh[i]='?'
print(msh)                                        