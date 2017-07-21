mylist = [1,3,5,34,6,2,8]

def sort(list):

    errors = int(len(list))
    while True:
        for i in list:
            while [i] <= int(len(list)):
                    if list[i+1] < list[i]:
                        bigger_number = list[i]
                        list[i] = list[i+1]
                        list[i+1] = bigger_number
                        errors -= 1
            if i > int(len(list)):
                i = 0
                errors = int(len(list))
        if errors == 0:
            break


    return list
    print(sort(mylist))


'''print("Unsorted:")
print(mylist)
print("Sorted")
print(sort(mylist))'''
