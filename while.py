numbers= []                 #program that continually asks the user to enter a number

while True:
    try:
      num =int(input("enter a number"))
      numbers.append(num)
    except ValueError:
        print("You entered an invalid input")
        
        
   
    if num ==-1:   #When the user enters “-1”, the program should stop requesting the user to enter a number
       numbers.pop()
       avg=sum(numbers)/(len(numbers))  
       break
    
print(avg)



  