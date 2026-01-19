def print_reversed_list_integer(my_list=[]):
    len_t = len(my_list) - 1 
    for i in range(len(my_list)):
        print(my_list[len_t-i])
