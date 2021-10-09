def check_list(list_in):
    count = 3
    lst = [1, 1, 5]
    for i in lst:
        if i in list_in:
            count -= 3
            list_in.remove(i)
            if count == 0:
                print("it's a match")
                break
        else:
            print("its gone")


list_in1 = [1, 5, 6, 4, 1, 2, 3, 5]
list_in2 = [1, 5, 6, 5, 1, 2, 3, 6]
check_list(list_in1)
check_list(list_in2)
