# """**CÂU 4:** Viết 4 functions để ước lượng các hàm số sin, cos, sinh, cosh"""

#NOTE FOR RANGE FUNCTION
# range(start, stop_not_included, step)

#Ham tinh giai thua
def factorial(n):
    result = 1
    for i in range(1, n + 1):  #from 1 to n
        result = result * i
    return result

#a) Ham tinh SIN
# approx_sin (x=3.14 , n =10)
# >> 0.0015926529267151343

def approx_sin(x, n):
    result = 0
    for i in range(0, n):
        result += (-1)**i * x**(2*i + 1) / factorial(2*i + 1)
    return result

#Goi ham de test:
print(f"approx_sin (x=3.14, n=10): {approx_sin(3.14, 10)}")


#b) Ham tinh COS
# approx_cos (x=3.14 , n =10)
# >> -0.9999987316527259

def approx_cos(x, n):
    result = 0
    for i in range(0, n):
        result += (-1)**i * x**(2*i) / factorial(2*i)
    return result

#Goi ham de test:
print(f"approx_cos (x=3.14, n=10): {approx_cos(3.14, 10)}")


#c) Ham tinh SINH
# approx_sinh (x=3.14 , n =10)
# >> 11.53029203039954
def approx_sinh(x, n):
    result = 0
    for i in range(0, n):
        result += x**(2*i + 1) / factorial(2*i + 1)
    return result

#Goi ham de test:
print(f"approx_sinh (x=3.14, n=10): {approx_sinh(3.14, 10)}")


#d) Ham tinh COSH
# approx_cosh (x=3.14 , n =10)
# >> 11.573574828234543

def approx_cosh(x, n):
    result = 0
    for i in range(0, n):
        result += x**(2*i) / factorial(2*i)
    return result

#Goi ham de test:
print(f"approx_cosh (x=3.14, n=10): {approx_cosh(3.14, 10)}")


#TRẮC NGHIỆM 9
print("\nTRAC NGHIEM 9: ")
assert round ( approx_cos (x=1, n =10) , 2) ==0.54
print ( round ( approx_cos (x=3.14 , n =10) , 2))

#TRẮC NGHIỆM 10
print("\nTRAC NGHIEM 10: ")
assert round ( approx_sin (x=1, n =10) , 4) ==0.8415
print ( round ( approx_sin (x=3.14 , n =10) , 4))

#TRẮC NGHIỆM 11
print("\nTRAC NGHIEM 11: ")
assert round ( approx_sinh (x=1, n =10) , 2) ==1.18
print ( round ( approx_sinh (x=3.14 , n =10) , 2))

#TRẮC NGHIỆM 12
print("\nTRAC NGHIEM 12: ")
assert round ( approx_cosh (x=1, n =10) , 2) ==1.54
print ( round ( approx_cosh (x=3.14 , n =10) , 2))