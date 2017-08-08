
mylist = [6,4,2]

end = mylist[len(mylist)-1] #the number 2
num_comp = mylist[end-1] #the number its being compared to, at this point the number after it (4)


for i in range(1,3):
    end = mylist[len(mylist)-i]
    num_comp = mylist[end-i]
    if end < num_comp:
        small_num = end
        del mylist[mylist.index(end)]
        mylist.insert(mylist.index(num_comp), small_num)
        print(mylist)
