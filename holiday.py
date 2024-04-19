
def hotel_cost(num_nights):
    return num_nights*250
    
def plane_cost(city_flight):
    ticket=0

    if city_flight == 1:
     ticket= 450
    elif city_flight == 2:
         ticket = 570
    elif city_flight== 3:
         ticket=700  
    else:
        print("You selected an invalid option")
    return ticket
   
def car_rental(rental_days):
    return rental_days*300
    
def holiday_cost(num_nights, city_flight,rental_days):
    hotel=hotel_cost(num_nights)
    plane=plane_cost(city_flight)
    car=car_rental(rental_days)
    return hotel + plane + car


city_flight=int(input("Where are you flying to (\n1.Qatar \n2.Doha \n3.Zanzibar): "))
num_nights=int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days=int(input("Enter the number of days for which you will be hiring a car: "))
    
total=holiday_cost(num_nights, city_flight,rental_days)
print(total) 