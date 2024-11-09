num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
check=int(input("Enter your selection:"))
if(check==1):
    result=num1+num2
    print("Result=",result)
elif(check==2):
    result=num1-num2
    print("Result=",result)
elif(check==3):
    result=num1*num2
    print("Result=",result)
elif(check==4):
    if(num2==0):
      print("Division by zero is not possible")
    else:
       result=num1/num2
       print("Result=",result)
else:
    print("You entered the wrong value")