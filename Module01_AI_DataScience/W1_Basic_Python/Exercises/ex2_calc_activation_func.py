# """**CÂU 2** Viết function mô phỏng theo 3 activation functions."""

import math

# Hàm cho trước để kiểm tra một số có phải float hay không
def is_number (n):
    try :
        float (n) # Type - casting the string to ‘float ‘.
        # If string is not a valid 'float'
        # it'll raise 'ValueError' exception
    except ValueError :
        return False
    return True

# Hàm kiểm tra tên activation
def is_activation (text):
    if (text == "sigmoid" or text == "relu" or  text == "elu" ):
        return True
    return False

# Hàm tính sigmoid
def calc_sig (x):
    return 1 / (1 + math.e**(-x))

# Hàm tính elu
def calc_elu (x):
    α = 0.01
    return α*(math.e**x - 1) if x <= 0  else  x

# Hàm tính relu
def calc_relu (x):
    return 0 if x <= 0  else  x

# Hàm chính cho Exercise 2
def calc_activation_func(x = None, act_name = None):  #None is null in Python
    # Yêu cầu user nhập x nếu không có thông số truyền vào hàm
    if (x == None):
        x = ( input(">> Input x = ") )
        if ( is_number(x) == False):
            print("x must be a float number")
            return

    # Yêu cầu user nhập act_name nếu không có thông số truyền vào hàm
    if (act_name == None):
        act_name = input("Input activation Function ( sigmoid | relu |elu ): ")
        if ( is_activation(act_name) == False):
            print(f"{act_name} is not supported")
            return

    #Tính giá trị activation và in ra kết quả
    x = float (x)
    if (act_name == "sigmoid"):
        result = calc_sig(x)
    elif (act_name == "relu"):
        result = calc_relu(x)
    elif (act_name == "elu"):
       result = calc_elu(x)

    print(f"{act_name}: f({x}) = {result}")
    return result

#Goi ham calc_activation_func()
calc_activation_func()

# TRẮC NGHIỆM 2:
print("\nTRAC NGHIEM 2: ")
assert is_number (3) == 1.0   #True is 1 in Python --> TRUE (no assesertion error)
assert is_number ('-2a') == 0.0 #False is 0 in Python --> TRUE (no assesertion error)
print ( is_number (1))  #TRUE
print ( is_number ('n')) #FALSE
#--> Choose option b

# TRẮC NGHIỆM 4:
print("\nTRAC NGHIEM 4: ")
assert round ( calc_sig (3) , 2) == 0.95
print ( round ( calc_sig (2) , 2))

# TRẮC NGHIỆM 5:
print("\nTRAC NGHIEM 5: ")
assert round (calc_elu (1)) ==1
print ( round (calc_elu (-1) , 2))


# TRẮC NGHIỆM 6:
print("\nTRAC NGHIEM 6: ")
assert calc_activation_func (x = 1, act_name ='relu') == 1
print ( round ( calc_activation_func (x = 3, act_name = 'sigmoid'), 2))

