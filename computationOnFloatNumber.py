# get number from user
user_number=float(input("please enter the number:"))
# calculatint...
slice_float_num=user_number%1
slice_int_num=user_number-slice_float_num
result=(slice_float_num*100)+(slice_int_num*10)
print(f'result=>{result}')