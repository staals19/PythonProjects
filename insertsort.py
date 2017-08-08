'''mylist = [6,2,4]

num_place = 0
end_num = 1
end = mylist[len(mylist)-end_num]

print(mylist)

for i in range(1,4):
    for i in range(1,4):
        if mylist.index(end) < mylist[mylist.index(end)-i]:
            small_num = mylist[mylist.index(end)]
            new_place = mylist.index(end)-i
            del mylist[mylist.index(end)]
            mylist.insert(new_place,small_num)
            print(i)
            print(mylist)
    end_num += 1
    end = mylist[len(mylist)-end_num]'''

mylist = [6,4,2]

end = mylist[len(mylist)] #the number 2
num_comp = mylist[end-1] #the number its being compared to, at this point the number after it

if end < num_comp:
    small_num = end
    del mylist[mylist.index(end)]
    mylist.insert(mylist)
