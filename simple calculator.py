def add(x,y):
 return x+y
def subtract(x,y):
 return x-y
def multiply(x,y):
 return x*y
def divide(x,y):
 return x/y
print ("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
    chioce = input("enter chioce(1/2/3/4):")
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number :"))
    if chioce == '1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif chioce == '2':
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif chioce =='3':
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif chioce == '4':
        print(num1,"/",num2,"=",divide(num1,num2))
    next_calculation = input("let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    
    else :
        print("invalid input")
      
