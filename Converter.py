def cup_to_grams(cups,conversion_rate):
    return cups*conversion_rate

def tablespoon_to_teaspoons(tablespoon):
    return tablespoon*3

def grams_to_cups(grams,conversion_rate):
    return grams/conversion_rate

def pounds_to_kilograms(pounds):
    return pounds*0.453592

def kilograms_to_pounds(kilograms):
    return kilograms*2.2

def meters_to_feet(meters):
    return meters*3.28

def feet_to_meters(feet):
    return feet*3048

def celcius_to_fahrenheit(celcius):
    return 1.8*celcius+32

def fahrenheit_to_celcius(fahrenheit):
    return fahrenheit-32/1.8
def converter():
    print("Welcome to the converter!")

    while True:
        print("Please Choose an option")
        print("1 - Convert cups to grams")
        print("2 - Convert tablespoons to teaspoons")
        print("3 - Convert grams to cups")
        print("4 - Convert pounds to kilograms")
        print("5 - Convert kilograms to pounds")
        print("6 - Convert meters to feet")
        print("7 - Convert feet to meters")
        print("8 - Convert celcius to fahrenheit")
        print("9 - Convert fahrenheit to celcius")
        print("10 - Exit program")
        choice=int(input("Enter one of the numbers above "))
        if choice == 1:
            cups = int(input("Enter the number of Cups "))
            conversion_rate = int(input("Enter the number of grams per cup you need "))
            print("Your result is",cup_to_grams(cups,conversion_rate),"grams")
         
        elif choice ==2:
            tablespoon = int(input("Enter the number of tablespoons "))
            print("Your result is:",tablespoon_to_teaspoons(tablespoon),"teaspoons")

        elif choice ==3:
            grams = int(input("Enter the number of grams "))
            conversion_rate = int(input("Enter the amount of grams per cup you need "))
            print("Your result is:",grams_to_cups(grams,conversion_rate),"Cups")
        
        elif choice == 4:
            pounds = int(input("Enter the number of pounds "))
            print("Your result is:",pounds_to_kilograms(pounds),"kilograms")
 
        elif choice == 5:
            kilograms = int(input("Enter the number of kilograms "))
            print("Your result is:",kilograms_to_pounds(kilograms),"pounds")

        elif choice == 6:
            meters = int(input("Enter the number of meters "))
            print("Your result is:",meters_to_feet(meters),"feet")

        elif choice == 7:
            feet = int(input("Enter the number of feet "))
            print("Your result is:",feet_to_meters(feet),"meters")
        
        elif choice ==8:
            celcius = int(input("Enter the temperature in celcius "))
            print("Your result is",celcius_to_fahrenheit(celcius),"degrees fahrenheit")
        
        elif choice ==9:
            fahrenheit = int(input("Enter the temperature in fahrenheit "))
            print("Your result is:",fahrenheit_to_celcius(fahrenheit),"degrees fahrenheit")

        elif choice ==10:
            print("Exiting program.....")
            break

        else:
            print("PLEASE PICK A NUMBER BETWEEN 1 AND 4 WHICH MEANS 1,2,3,4,5,6.7,9 OR 10 DONT INCLUDE THE COMMAS AND PLEASE DONT USE SPACES")
converter()