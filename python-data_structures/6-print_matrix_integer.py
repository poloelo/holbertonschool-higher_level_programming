def print_matrix_integer(matrix=[[]]):
    for row in matrix : 
        s_row = ""
        r_row = len(row)
        for i, element in enumerate(row) :
            if i == r_row - 1 :
                print(element, end="")
            else : 
                print(element, end=" ")
        print(s_row)
    return s_row
