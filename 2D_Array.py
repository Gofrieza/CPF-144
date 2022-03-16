row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
a_list = [[0 for column in range(col_num)] for row in range(row_num)]
print(a_list)
for row in range(row_num):
    for column in range(col_num):
        a_list[row][column] = row*column

print(a_list)
print(type(a_list))
