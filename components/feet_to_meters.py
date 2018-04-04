# 1 ft = 0.03048




#ask user if they want to convert feet to meters or meters to feet.


print(raw_input("Do you want to convert feet to meters? (Y/N)  "))
if raw_input == "y".capitalize():
    feet = float(raw_input("Enter feet "))
    feet_to_meters = feet * 0.3048 
    print ("{} is {} in meters".format(feet, feet_to_meters))
#if input not numeric print
#elif raw_input.isalpha = false 
else:
    meters = float(raw_input("Enter meters "))
    meters_to_feet = meters / 0.3048
    print ("{} is {} feet".format(meters, meters_to_feet))