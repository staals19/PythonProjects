mylist = [70,8,1,3,4,10,80]

errors = 0

while errors > -1:
    for i in range(0,len(mylist)-1):
        if mylist[i+1] < mylist[i]:
            bigger_number = mylist[i]
            mylist[i] = mylist[i+1]
            mylist[i+1] = bigger_number
            errors +=1
        else:
            errors -= 1

print(mylist)
