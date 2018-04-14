import math
from math import cos, sin, sqrt, asin
from random import randint, uniform

def mini_menu():
    """Goin' the distance's mini main menu is a REPL and allows the user to call functions"""
    
    print
    
    #asks user for input
    
    
    user_choice = int(raw_input("Choose your menu item -->   "))
    
    if user_choice == 1:
        #menu item 1 is calculate flat surface distance
        flat_surface()
    
    if user_choice == 2:
        #menu item 2 is calculate haversine distance
        haversine()
    
    #if user_choice == 3:
    #menu item 3 is calculate vincentys formulae
    
    #if user_choice == 4:
    #menu item 4 is calculate distance using all three
    #   flat_surface
    #  haversine()
    
    if user_choice == 3:
        #menu item 5 is convert lat and long to radians
        decimal_degrees_to_radians()
    
    if user_choice == 4:
        #menu item 6 is convert miles to meters
        miles_to_meters()
    
    if user_choice == 5:
        #menu item 7 is random coordinate generator
        random_coordinate()
    
    if user_choice == 6:
        about()
    
    if user_choice == 7:
        exit()

def get_starting_latitude():
    """gets the starting latitude"""
    invalid_lat = True
    
    
    while invalid_lat:
        starting_latitude = (int(raw_input("Please enter starting latitude -->  ")))
        
        if starting_latitude < 180.9999 and starting_latitude > -180.9999:
            invalid_lat = False
            return starting_latitude
        
        else:
            invalid_lat = True




def get_ending_latitude():
    """gets the starting latitude"""
    invalid_lat = True
    
    
    while invalid_lat:
        ending_latitude = (int(raw_input("Please enter ending latitude -->  ")))
        
        if ending_latitude < 180.9999 and ending_latitude > -180.9999:
            invalid_lat = False
            return ending_latitude
        
        else:
            invalid_lat = True



def get_ending_longitude():
    """gets the ending latitude"""
    
    invalid_long = True
    
    
    while invalid_long:
        ending_longitude = (int(raw_input("Please enter ending longitude -->  ")))
        
        if ending_longitude < 90.9999 and ending_longitude > -90.9999:
            invalid_long = False
            
            return ending_longitude
        
        
        else:
            invalid_long = True

def get_starting_longitude():
    """gets the ending latitude"""
    
    invalid_long = True
    
    while invalid_long:
        starting_longitude = (int(raw_input("Please enter starting longitude -->  ")))
        
        if starting_longitude < 90.9999 and starting_longitude > -90.9999:
            
            invalid_long = False
            
            return starting_longitude
        
        
        else:
            invalid_long = True

earth_radius = 3959

def flat_surface():
    """makes a flat surface measurement using pythagorean theorem"""
    start_latitude = get_starting_latitude()
    start_longitude = get_starting_longitude()
    end_latitude = get_ending_latitude()
    end_longitude = get_ending_longitude()
    
    x = (end_latitude - start_latitude) * cos((end_longitude + start_longitude)/2)
    y = (end_longitude - start_longitude)
    flat_surface_distance = earth_radius * (sqrt(x**2 + y **2))
    print "\n{} is the flat surface distrance in miles.".format(flat_surface_distance)
    mini_menu()


def haversine():
    start_latitude = get_starting_latitude()
    start_longitude = get_starting_longitude()
    end_latitude = get_ending_latitude()
    end_longitude = get_ending_longitude()
    
    """Haversine formula for calculating distance"""
    #calculate the change or difference in latitudes
    difference_lat = (0.010174533 * (end_latitude - start_latitude))
    #calculate the change or difference in longitudes
    difference_long = (0.010174533 * (end_longitude - end_latitude))
    #lat in radians
    start_latitude = (0.010174533 * start_latitude)
    #long in radians
    end_latitude = (0.010174533 * end_latitude)
    
    #now that conversions from lat long to radians are complete time formula
    
    #value of a is necessary for value of c
    a = sin(difference_lat/2)**2 + cos(start_latitude) * cos(end_latitude) * sin(difference_long/2)**2
    
    #almost there
    c = 2 * asin(sqrt(a))
    
    haversine_distance = earth_radius * c
    
    print "\n{} is the Haversine distance in miles.".format(haversine_distance)
    mini_menu()

#return distance

def miles_to_meters():
    """takes parameters and converts from meters to miles"""
    
    
    miles_to_meters = (float(raw_input("Enter the miles you want to convert to meters -->  ")))
    
    meters = miles_to_meters * 1609
    
    print "{} miles is {} meters".format(miles_to_meters, meters)

def decimal_degrees_to_radians():
    """take decimal degree coordinate pairs and convert to radians"""
    print "This will take maximum 2 coordinate pairs and convert them to radians"
    start_latitude = get_starting_latitude()
    start_longitude = get_starting_longitude()
    end_latitude = get_ending_latitude()
    end_longitude = get_ending_longitude()
    
    degrees_to_radian = 0.01074533
    
    
    start_latitude_radian = start_latitude * degrees_to_radian
    start_longitude_radian = start_longitude * degrees_to_radian
    end_latitude_radian = end_latitude  * degrees_to_radian
    end_longitude_radian = end_longitude * degrees_to_radian
    print "\n[{}, {}] , [{}, {}]".format(start_latitude_radian, start_longitude_radian, end_latitude_radian, end_longitude_radian)
    mini_menu()


#random coordinate generator
def random_coordinate():
    """Prints a random number"""
    random_latitude = uniform(-180.9999,181)
    random_longitude = uniform(-90.9999,91)
    random_latitude = round(random_latitude, 4)
    random_longitude = round(random_longitude, 4)
    #too many significant digits are yeilded from the uniform function let's truncate
    print"({} , {})".format(random_latitude, random_longitude)
    mini_menu()


def about():
    """about program section"""
    print"----------------------------------------------------------------------------------------------------------------"
    print"                                                                                                                "
    print"                                                                                                                "
    print"  _____         _         _    _    _                  _  _       _                                             "
    print"  |  __ \       (_)       ( )  | |  | |                | |(_)     | |                                          "
    print"  | |  \/  ___   _  _ __  |/   | |_ | |__    ___     __| | _  ___ | |_   __ _  _ __    ___   ___               "
    print"  | | __  / _ \ | || '_ \      | __|| '_ \  / _ \   / _` || |/ __|| __| / _` || '_ \  / __| / _ \    "
    print"  | |_\ \| (_) || || | | |     | |_ | | | ||  __/  | (_| || |\__ \| |_ | (_| || | | || (__ |  __/     "
    print"   \____/ \___/ |_||_| |_|      \__||_| |_| \___|   \__,_||_||___/ \__| \__,_||_| |_| \___| \___|           "
    print"----------------------------------------------------------------------------------------------------------------"
    print"----------------------------------------------------------------------------------------------------------------"
    print"----------------------------------------------------------------------------------------------------------------"
    print"Annijke Wade - 2018"
    print"github.com/geodesicdome/goin_the_distance"
    print"adewade@gmail.com"
    print
    mini_menu()

#call the function
def main_menu():
    """Goin' the distance's main menu is a REPL and allows the user to call functions"""
    print"----------------------------------------------------------------------------------------------------------------"
    print"                                                                                                                "
    print"                                                                                                                "
    print"   _____         _         _    _    _                  _  _       _                                             "
    print"  |  __ \       (_)       ( )  | |  | |                | |(_)     | |                                          "
    print"  | |  \/  ___   _  _ __  |/   | |_ | |__    ___     __| | _  ___ | |_   __ _  _ __    ___   ___               "
    print"  | | __  / _ \ | || '_ \      | __|| '_ \  / _ \   / _` || |/ __|| __| / _` || '_ \  / __| / _ \    "
    print"  | |_\ \| (_) || || | | |     | |_ | | | ||  __/  | (_| || |\__ \| |_ | (_| || | | || (__ |  __/     "
    print"   \____/ \___/ |_||_| |_|      \__||_| |_| \___|   \__,_||_||___/ \__| \__,_||_| |_| \___| \___|           "
    print"----------------------------------------------------------------------------------------------------------------"
    print"----------------------------------------------------------------------------------------------------------------"
    print"----------------------------------------------------------------------------------------------------------------"
    
    #menu options and welcome message show
    
    print
    print "             Welcome to Goin' the Distance!\n"
    print "This program allows you to calculate distance utlizing three different methods:"
    print " Flat surface distance, Haversine Formula, and Vincenty's Formulae"
    print "You can also convert your coordinates to Radians, convert miles to meters"
    print "and generate random coordates!\n"
    print "             1 -- CALCULATE FLAT SURFACE DISTANCE"
    print "             2 -- CALCULATE HAVERSINE DISTANCE"
    #  print "             3 -- CALCULATE VINCENTY'S FORMULAE"
    #  print "             4 -- CALCULATE DISTANCE USING ALL THREE METHODS"
    print "             3 -- CONVERT LATITUDE AND LONGITUDE TO RADIANS"
    print "             4 -- CONVERT MILES TO METERS"
    print "             5 -- RANDOM COORDINATE GENERATOR"
    print "             6 -- ABOUT"
    print "             7 -- EXIT"
    print
    
    #asks user for input
    
    
    user_choice = int(raw_input("Choose your menu item -->   "))
    
    if user_choice == 1:
        #menu item 1 is calculate flat surface distance
        flat_surface()
    
    if user_choice == 2:
        #menu item 2 is calculate haversine distance
        haversine()
    
    #if user_choice == 3:
    #menu item 3 is calculate vincentys formulae
    
    #if user_choice == 4:
    #menu item 4 is calculate distance using all three
    #   flat_surface
    #  haversine()
    
    if user_choice == 3:
        #menu item 5 is convert lat and long to radians
        decimal_degrees_to_radians()
    
    if user_choice == 4:
        #menu item 6 is convert miles to meters
        miles_to_meters()
    
    if user_choice == 5:
        #menu item 7 is random coordinate generator
        random_coordinate()
    
    if user_choice == 6:
        about()
    
    if user_choice == 7:
        exit()

main_menu()



