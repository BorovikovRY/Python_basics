from os import remove

list_number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
result_remove = 0
result_remove += list_number.pop(-1)
result_remove += list_number.pop(0)
result_remove += list_number.pop(12)
result_remove += list_number.pop(7)
print(list_number)
print(result_remove)