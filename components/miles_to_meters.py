# 1 mile = 1609.34




#ask user if they want to convert feet to meters or meters to feet.


print(raw_input("Do you want to convert miles to meters? (Y/N)  "))

if raw_input == "y".capitalize():
    miles = float(raw_input("Enter miles "))
    miles_to_meters = 1609 * miles 
    print ("{} is {} in meters".format(miles, miles_to_meters))
#elif raw_input.isalpha = false 
#else:
 #   meters = float(raw_input("Enter meters "))
  #  meters_to_miles = meters / 1609.34
   # print ("{} miles is {} meters".format(meters, meters_to_miles))
    

