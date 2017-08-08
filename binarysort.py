mylist = [1,2,3,4,5,6,7,8,9,10]

num = int(input("what number?"))

def findMiddle(list):
    middle = float(len(list))/2
    if middle % 2 != 0:
        return list[int(middle + .5)]
    else:
        return list[int(middle)]

run = True

while run == True:
    if int(len(mylist)) == 1:
        if mylist == [num]:
            print("true")
            break
        else:
            print("false")
            break

    middle_num = findMiddle(mylist)

    if middle_num == num:
        print("true")
        run = False

    if middle_num >= num:
        del mylist[mylist.index(middle_num):len(mylist)]
    else:
        del mylist[0:mylist.index(middle_num)]
