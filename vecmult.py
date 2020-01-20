matrix1 = [[1,3,2], [1,2,3]]
matrix2 = [[1,2,3], [2,1,3]]
total = []
for matrix1_sublist, matrix2_sublist in zip(matrix1,matrix2):
    total.append ([matrix1_sublist_item + matrix2_sublist_item for matrix1_sublist_item, matrix2_sublist_item in zip(matrix1_sublist, matrix2_sublist)])


print(total)