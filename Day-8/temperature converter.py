# Temperature Converter
# Create functions to convert:
# - Celsius to Fahrenheit
# - Fahrenheit to Celsius

def fahrenheit_convert(x):
    x=(9*C+160)/5
    return x

def celsius_convert(y):
    y=(5*F-160)/9
    return y

print("Convert to:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

num=int(input("Enter your choice: "))
if num==1:
    C=int(int(input("Enter Celsius Degree: ")))
    print("You have entered: ",C)
    result_fahrenheit=fahrenheit_convert(C)
    print("The temperature in Fahrenheit is: ",result_fahrenheit)
elif num==2:
    F=int(int(input("Enter Fahrenheit Degree: ")))
    print("You have entered: ",F)
    result_celsius=celsius_convert(F)
    print("The temperature in Celsius is: ",result_celsius)
else:
    print("Invalid choice!")