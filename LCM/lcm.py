
# L.C.M of 2 numbers , with inputs from the user


def cal_lcm(first_num, second_num):

    if first_num > second_num:
        value = first_num
    else:
        value = second_num

    while(True):
        if((value % first_num == 0) and (value % second_num == 0)):
            lcm = value
            break
        value += 1

    print(f'The L.C.M  is {lcm} ')


input1 = input("Type the first value : ")
input1 = int(input1)

input2 = input("Type in the second value : ")
input2 = int(input2)

cal_lcm(input1, input2)
