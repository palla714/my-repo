x = int(input("enter the row number"))

for i in range(x):
    #print(' '*(x-i)+'*'*(2*i+1))
    print('*'*(i+1)+' '*(x-i))
    #print(i)