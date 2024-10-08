num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /): ") 
addition = num1 + num2 
subraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 

match operation:
    case "+":
        print("The result is", addition)
    case "-":
        print("The result is", subraction)
    case "*":
        print("The result is", multiplication)
    case "/": 
        print("The result is", division)
    case _:
        print("Input correct operation") 

    





    


    

 