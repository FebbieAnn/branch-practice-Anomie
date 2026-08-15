x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operator = input("Enter operator (Sum or Difference): ")


match operator:
 case "Sum":
    sum = int(x) + int(y)    
    print("Addition: ", sum)
 case "Difference" :
    dif = int(x) - int(y)    
    print("Difference: ", dif)



