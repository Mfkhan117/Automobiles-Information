# Import pandas package
import pandas as pd

# Automobile class setup
class Automobile:
    def __init__(self,type,make,model,year,cost,mpg,tanksize,trip,totalcost):  # Constructor to initialize values
        self.type = type  # Type of car
        self.make = make  # Make of car
        self.model = model  # Model of car
        self.year = year  # Year of car
        self.cost = cost  # Cost of car
        self.mpg = mpg  # MPG the car has
        self.tanksize = tanksize  # Gas tank/Battery size of the car
        self.trip = trip  # Trip cost for user specified destination and miles
        self.totalcost = totalcost  # Total cost of Car with the trip

    # Function to calculate trip cost
    def tripcost(self,city,miles):
     if self.type == 'electric':  # If the car is electric
        self.trip = round(33.7 * 0.14 * (miles/self.mpg) ,2)  # Electric cost is $0.14 per charge * 33.7 per gallon for MPGe
        print("Your total round trip cost between " + str(city) + " and Detroit for your "
             + str(self.year) + " " + self.make + " " + self.model + " is: $" + str(round(self.trip, 2)))
        self.totalcost = round(self.cost + self.trip,2)  # Set the total cost
     elif self.type == 'gas':  # If the car runs on gas
        self.trip = round(4.39 * (miles/self.mpg),2)  # Gas cost is $4.39 per gallon
        print("Your total round trip cost between " + str(city) + " and Detroit for your "
             + str(self.year) + " " + self.make + " " + self.model + " is: $" + str(round(self.trip, 2)))
        self.totalcost = round(self.cost + self.trip,2)  # Set the total cost
     elif self.type == 'diesel':  # If the car is a diesel
        self.trip = round(5.15 * (miles/self.mpg),2)  # Diesel gas cost is $5.15 per gallon
        print("Your total round trip cost between " + str(city) + " and Detroit for your "
              + str(self.year) + " " + self.make + " " + self.model + " is: $" + str(round(self.trip, 2)))
        self.totalcost = round(self.cost + self.trip,2)  # Set the total cost
     print('\n')
     return round(self.totalcost,2)  # Return the total cost for each car


totalcost = 0
trip = 0

# Constant Cars
CAR_1 = Automobile('electric','Toyota','Corolla',2022,23750.00,53.0,1.3,0,0)
CAR_2 = Automobile('gas','Chevy','Malibu',2022,23400.00,32.0,15.8,0,0)
CAR_3 = Automobile('diesel','Ford','F150',2022,29990.00,25.0,26.0,0,0)

# # User will input the 4th car
type = str(input("Enter the type of car, must be gas,electric or diesel: "))
while(type != 'gas' and type != 'electric' and type != 'diesel'):
    print("Error: Vehicle type must be 'gas','electric', or 'diesel'")
    type = str(input("Enter the type of car, must be gas,electric or diesel: "))

make = str(input("Enter the make: "))
model = str(input("Enter the model: "))
year = int(input("Enter the year: "))
cost = float(input("Enter the cost: "))
mpg = float(input("Enter the MPG: "))
tanksize = float(input("Enter the tanksize: "))
print('\n')

# The parameters of the car will equal what the user specified
CAR_4 = Automobile(type,make,model,year,cost,mpg,tanksize,trip,totalcost)

# User will input the 5th car
type = str(input("Enter the type of car, must be gas,electric or diesel: "))
while(type != 'gas' and type != 'electric' and type != 'diesel'):
     print("Error: Vehicle type must be 'gas','electric', or 'diesel'")
     type = str(input("Enter the type of car, must be gas,electric or diesel: "))

make = str(input("Enter the make: "))
model = str(input("Enter the model: "))
year = int(input("Enter the year: "))
cost = float(input("Enter the cost: "))
mpg = float(input("Enter the MPG: "))
tanksize = float(input("Enter the tanksize: "))
print('\n')

CAR_5 = Automobile(type,make,model,year,cost,mpg,tanksize,trip,totalcost)

# User will input the 6th car
type = str(input("Enter the type of car, must be gas,electric or diesel: "))
while(type != 'gas' and type != 'electric' and type != 'diesel'):
    print("Error: Vehicle type must be 'gas','electric', or 'diesel'")
    type = str(input("Enter the type of car, must be gas,electric or diesel: "))

make = str(input("Enter the make: "))
model = str(input("Enter the model: "))
year = int(input("Enter the year: "))
cost = float(input("Enter the cost: "))
mpg = float(input("Enter the MPG: "))
tanksize = float(input("Enter the tanksize: "))
print('\n')

CAR_6 = Automobile(type,make,model,year,cost,mpg,tanksize,trip,totalcost)

# User will specify the City destination and total miles from Detroit
city = str(input("What City are you traveling too?: "))
miles = int(input("How many miles will you travel?: "))
print('\n')

# Based on users input of the destination each cars tripcost will be calculate in the tripcost function
trip1 = CAR_1.tripcost(city,miles)
trip2 = CAR_2.tripcost(city,miles)
trip3 = CAR_3.tripcost(city,miles)
trip4 = CAR_4.tripcost(city,miles)
trip5 = CAR_5.tripcost(city,miles)
trip6 = CAR_6.tripcost(city,miles)

# Print out the Vehicle specifications of each car
print("Vehicle Specifications: ")
# Using Panda print out an organized Table of the list of cars
cartypes = [[CAR_1.type,CAR_1.model,CAR_1.make,CAR_1.year,CAR_1.cost,CAR_1.mpg,CAR_1.tanksize,CAR_1.trip,CAR_1.totalcost],
            [CAR_2.type,CAR_2.model,CAR_2.make,CAR_2.year,CAR_2.cost,CAR_2.mpg,CAR_2.tanksize,CAR_2.trip,CAR_2.totalcost],
            [CAR_3.type,CAR_3.model,CAR_3.make,CAR_3.year,CAR_3.cost,CAR_3.mpg,CAR_3.tanksize,CAR_3.trip,CAR_3.totalcost],
            [CAR_4.type,CAR_4.model,CAR_4.make,CAR_4.year,CAR_4.cost,CAR_4.mpg,CAR_4.tanksize,CAR_4.trip,CAR_4.totalcost],
            [CAR_5.type,CAR_5.model,CAR_5.make,CAR_5.year,CAR_5.cost,CAR_5.mpg,CAR_5.tanksize,CAR_5.trip,CAR_5.totalcost],
            [CAR_6.type,CAR_6.model,CAR_6.make,CAR_6.year,CAR_6.cost,CAR_6.mpg,CAR_6.tanksize,CAR_6.trip,CAR_6.totalcost]]

df = pd.DataFrame(cartypes, columns=['Type','Model','Make','Year','Cost$','MPG/e','Tanksize','Trip$','Totalcost$'])
print(df)