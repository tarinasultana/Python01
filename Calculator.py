print('''
        1.Add(+) 2.Subtract(-) 3.Multiply(*) 4.Divide(/)
        5.Power(^) 6.Root 7.Modulus 8.Pie
        9.
''')
select = int(input("Select an operations  :")) 
  
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
  
if select == 1: 
    print(num1+num2)
  
elif select == 2: 
    print(num1-num2)
  
elif select == 3: 
    print(num1*num2) 
  
elif select == 4: 
    print(num1/num2)
      
else: 
    print("Invalid input") 