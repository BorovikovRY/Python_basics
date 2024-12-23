num1 = int (input('write three positive integers number: '))
num2 = int (input('write three positive integers number: '))
num3 = int (input('write three positive integers number: '))
result1 = (num1 + num2) * num3
result2 = num1 + (num2 * num3)
result3 = (num1 * num2) + num3
result4 = num1 * (num2 + num3)
result5 = num1 * num2 * num3
print (max (result1,result2,result3,result4,result5))