lowerLim = int(input("Enter the lower limit: "))
upperLim = int(input("Enter the upper limit: "))
divisor = int(input("Enter the number to be divided by: "))

for i in range(lowerLim, upperLim+1):
    if i % divisor == 0:
        print(i)


# 5 % 3 --> 2 --> % is called modulus operator and it returns remainder






