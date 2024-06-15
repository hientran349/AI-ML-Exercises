# **CÂU 1**. Viết function thực hiện đánh giá classification model bằng F1-Score

import math

def calc_f1_score(tp, fp, fn):
    #In ra ten ham va gia tri thong so dau vao
    print(f"\n{calc_f1_score.__name__}(tp={tp}, fp={fp}, fn={fn})")

    #KIEM TRA GIA TRI DAU VAO

    #Kiem tra gia tri dau vao duoc nhap boi user
    # try:
    #     fp = int ( input ("fp = ") )
    # except ValueError:
    #     print("fp must be int")
    #     return

    #Kiem tra gia tri dau vao cua ham
    if not isinstance(tp, int):     #can replace by type(tp) != int
        print(">> tp must be int")
        return

    if not isinstance(fp, int):
        print(">> fp must be int")
        return

    if not isinstance(fn, int):
        print(">> fn must be int")
        return

    if (tp <= 0 or fp <= 0 or fn <= 0):
        print(">> tp and fp and fn must be greater than zero")
        return

    #Tinh ket qua
    precision = tp/(tp + fp)
    recall = tp/ (tp + fn)
    f1_score = 2*precision * recall/(precision + recall)
    print(f">> precision is {precision}" )
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")

    return f1_score #Yeu cau cua trac nghiem 1

#Goi ham calc_f1_score() de chay va kiem tra
calc_f1_score (tp=2, fp=3, fn=4)
calc_f1_score (tp='a',fp=3, fn=4)
calc_f1_score (tp=2, fp='a', fn=4)
calc_f1_score (tp=2, fp=3, fn='a')
calc_f1_score (tp=2, fp=3, fn=0)
calc_f1_score (tp=2.1, fp=3, fn=0)

#Note: Keyword arguments (or named arguments) in Python (the order of arguments may be changed)
#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp


#TRAC NGHIEM 1:
print("\nTRAC NGHIEM 1: ")
assert round ( calc_f1_score (tp =2, fp =3, fn =5) , 2) == 0.33
#Ham assert se bao loi AssertionError neu ket qua la FALSE

print ( round ( calc_f1_score (tp =2, fp =4, fn =5) , 2))
#Kết quả assert ở trên là TRUE, nên chương trình chạy tiếp, in ra kết quả ở đây là 0.31
#--> Choose option c

#Note: Keyword arguments (or named arguments) in Python (the order of arguments may be changed)
#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp
