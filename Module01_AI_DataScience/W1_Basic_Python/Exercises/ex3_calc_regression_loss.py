#"""**CÂU 3**: Viết function lựa chọn regression loss function để tính loss:"""

import random
import math

# Hàm tính Absolute Error
def calc_ae (y, y_hat ):
    return abs(y - y_hat)

# Hàm tính Absolute Error
def calc_se (y, y_hat ):
    return (y - y_hat)**2

# HÀM CHÍNH CHO QUESTION 3
def regression_loss():
    #Input number of samples
    num_samples = input("Input number of samples ( integer number ) which are generated : ")
    if (not num_samples.isnumeric()) :
        print("num_samples must be an integer number")
        return

    num_samples = int(num_samples)

    #Input loss name (MAE, MSE)
    #Mean Absolute Error (MAE)
    #Mean Squared Error (MSE)
    #Root Mean Squared Error (RMSE)
    loss_name = input("Input loss name (MAE | MSE| RMSE): ")
    if (loss_name != "MAE" and loss_name != "MSE" and loss_name != "RMSE"):
        print(f"{loss_name} is not supported")
        return

    #Data for each sample
    #loss name : RMSE , sample : 0, pred : 6.659262156575629 , target : 4.5905830130732355 ,
    #  loss : 4.279433398761796

    #Create data for each sample and calculate loss
    sum = 0
    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)
        print(f"loss name : {loss_name}, sample : {i}, pred : {pred}, target : {target},")

        #Calculate loss
        if (loss_name == "MAE"):
            loss = abs(pred - target)
            print(f"    loss: {loss}")
            sum += loss

        else: # MSE or RMSE
            squared_loss = (pred - target)**2
            print(f"    loss: {squared_loss}")
            sum += squared_loss

    #Calculate final loss
    if (loss_name == "MAE" or loss_name == "MSE"):
        final_loss = sum/num_samples
    elif (loss_name == "RMSE"):
        final_loss = math.sqrt(sum/num_samples)

    print(f"final {loss_name} : {final_loss}")

#Goi ham regression_loss()
regression_loss()


#TRẮC NGHIỆM 7
print("\nTRAC NGHIEM 7: ")
y = 1
y_hat = 6
assert calc_ae (y, y_hat )==5
y = 2
y_hat = 9
print ( calc_ae (y, y_hat ))

#TRẮC NGHIỆM 8
print("\nTRAC NGHIEM 8: ")
y = 4
y_hat = 2
assert calc_se (y, y_hat ) == 4
print ( calc_se (2, 1))