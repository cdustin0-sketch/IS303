print("Road Trip Planner")

#Ask them the questions
#float makes it so the output can be numbers
#input makes a response possible

travaler_name = input("What is your name? ")
destination = input("Where are you traveling? ")
one_way_miles = float(input("How many miles is the trip one way? "))
vehicles_miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))
gas_price = float(input("What is the gas price per gallon? "))
num_travelers = int(input("How many travelers are going? "))

#run the calculations
#round trip is there and back so need to double
total_miles = one_way_miles * 2

#gallons needed is total miles divided by mpg on car
gallons_needed = total_miles / vehicles_miles_per_gallon

#total cost of the gas is gallons of gas times the price
total_gas_cost = gallons_needed * gas_price

#Cost per traveler is total gas divide by how many people are going
cost_per_traveler = total_gas_cost / num_travelers



#Now we show the trip summary and all the outcomes

print("=======================")
print("Trip Summary")
print("=======================")

print(f"Traveler:  {travaler_name.upper()}")
print(f"Destination: {destination}")
print(f"Gallons of Gas: {gallons_needed:.0f}")
print(f"Gas Cost: ${total_gas_cost:.2f}")
print(f"Cost Per Traveler: ${cost_per_traveler:.2f}")

#I am done but I will wish them a great trip
print("========================")
print("Have a great trip!")

#I am so done with this lesson
