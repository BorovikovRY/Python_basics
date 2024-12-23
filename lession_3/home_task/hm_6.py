# coast_penсil = 3
# coast_pen = coast_penсil + 2
# coast_marker = coast_pen + 7
# pencil = int(input('enter quantity: '))
# pen = int(input('enter quantity: '))
# marker = int(input('enter quantity: '))
# result_pencil =  pencil * coast_penсil
# result_pen = coast_pen * pen
# result_marker = coast_marker * marker
# all_result = result_pencil + result_pen + result_marker
# print(all_result)


coast_penсil = 3
coast_pen = coast_penсil + 2
coast_marker = coast_pen + 7
pencil, pen, marker = map(int,input('enter quantity: ').split())
result_pencil =  pencil * coast_penсil
result_pen = coast_pen * pen
result_marker = coast_marker * marker
all_result = result_pencil + result_pen + result_marker
print(all_result)


