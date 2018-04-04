#prompt user for inputs in coordinates and calculate disntace 
#milimeter precision


print "Welcome to Goin' the Distance, a programatic way to calculate distance."
print "Goin' the Distance takes in two sets of coordinate pairs and"
print "calculates distance based on three different methods"
print "Flat surface distance, Haversine Formula, and Vincenty's Formulae"

import math

starting_latitude = float(raw_input("Please enter starting latitude -->  "))

if starting_latitude >= -180.99999999 or starting_latitude <= 180.99999999:
    print "Thanks"
else: 
    print "Please enter a valid latitude"

starting_longitude = float(raw_input("Please enter starting longitude -->  "))

if starting_latitude >= -90.99999999 or starting_latitude <= 90.99999999:
    print "Thanks"
else: 
    print "Please enter a valid longitude"
    
print
print "Starting latitude, longitude ({},{})".format(starting_latitude, starting_longitude)
print

ending_latitude = float(raw_input("Please enter ending latitude -->  "))

if ending_latitude >= -180.99999999 or ending_latitude <= 180.99999999:
    print "Thanks"
else: 
    print "Please enter a valid latitude"

ending_longitude = float(raw_input("Please enter ending longitude -->  "))

if ending_latitude >= -90.99999999 or ending_latitude <= 90.99999999:
    print "Thanks"
else: 
    print "Please enter a valid longitutde"


print
print "Ending latitude, longitude ({},{})".format(ending_latitude, ending_longitutde)
print

#while 
#raw_input("Are these coordinate pairs correct? ({}, {}), ({},{}) Y/N  --> ".format(starting_latitude, starting_longitude, ending_latitude, ending_longitude))
  #  if raw_input = "y".capitalize
      #  need to print cool time to move forward
    
  #  else:
    #    needs to loop back to top of program

#save coordinates as start and end

start = starting_latitude, starting_longitude

end = ending_latitude, ending_longitude

print "{} & {}"
        

#loop back to top after 


#need to convert lat long into decimal degrees


#decimal degrees = degrees + minutes/60 + seconds/300

#starting_latitude[]


#radius of earth 

#haversine 

Radius = 6371000


#print haversine 