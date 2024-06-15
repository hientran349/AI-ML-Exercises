# """**CÂU 5:** Viết function thực hiện Mean Difference of nth Root Error"""

# md_nre_single_sample (y=100 , y_hat =99.5 , n=2, p=1)
# >> 0.025031328369998107
#
# md_nre_single_sample (y=50 , y_hat =49.5 , n=2, p=1)
# >> 0.03544417213033135

def MD_nRE_loss():
    #Input
    #Giả sử rằng các điều kiện input đầu vào đều được đáp ứng (không cần kiểm tra)

    y = float( input("Input y = ") )
    y_hat = float( input("Input y_hat = ") )
    n = int( input("Input n = ") )
    p = int ( input("Input p = ") )

    #Calculate MD_nRE:
    loss = (y**(1/n) - y_hat**(1/n))**p
    print(f"MD_nRE loss: {loss}")

#Goi ham MD_nRE_loss()
MD_nRE_loss()