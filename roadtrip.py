# SDM: I want to create a series of functions so that when I run my program, it will help me to plan my road trip, 
#      where I have a car, I have some money, my car has a full tank of gas to start, the tank has a size (gallons
#      it can hold), the car has a fuel efficiency in miles per gallon, there is a fixed price of gasoline in dollars 
#      per gallon, and I have a destination in mind that is some number of miles away from home.
#      Bonus points: I have some friends / family who I want to take with me and I'd lke to split the travel costs 
#      equally.

# What things do I want to know that are relevant to my road trip?
# 1) How many gallons of gas do I need to get to my destination?
# 2) How many times will I need to stop for gas?
# 3) How many hours/minutes will my trip take?
# 4) How much money will the trip cost me?
# 5) Can I even make the trip given the initial money and gas amounts as well as how much more money would I need to complete it?
# 6) Given how much money I have and given how much the trip costs, I would need how many people paying equal amounts to afford it?

# List out our things that we have in the program already,

print("This program will answer for you some relevant questions for any road trip that you choose to go on.")
print("First, I would like to ask you some questions concerning certain factors to help me calculate your answers.")

initial_money = float(input("How much money do you have when you start out?:" )) # in dollars or cents
tank_size = int(input("How many gallons of fuel can your vehicle hold in its tank?:" )) # in gallons
mpg = int(input("How fuel efficient is your car in miles per gallon?:" )) # for fuel efficiency
ppg = float(input("What is the current price per galloon for the fuel you use in the are you are travelling in?:" )) # price for cost
distance = int(input("How far is your destination from where you are starting out from in miles?:" )) # in miles
avg_speed = int(input("How fast on average will you be traveeling at while on this roadtrip?:" )) # in miles per hour

# To answer Question #1, we need to figure out the total amount of gallons required for the trip from the total distance and the fuel efficiency of the vehicle.
def calc_full_trip_gall(size, num):
    return size / num

full_trip_gall = calc_full_trip_gall(distance, mpg)
print(f"To reach your destination, your vehicle will need to consume {full_trip_gall} gallons.")

# To answer Question #2, we need to figure out the total amount of times that one needs to stop for gas on the trip from the distance per tank and the total distance.

full_tank_dist = distance // mpg

def calc_num_times_stop(dist_per_tank, dist_total):
    return dist_total // dist_per_tank

num_times_stop = calc_num_times_stop(full_tank_dist, distance)
print(f"To travel to your destination, you will need to stop at least {num_times_stop} times.")

# To answer Question #3, we need to figure out how long it will take for the trip to finish from the total distance and the average speed travelling.
def calc_travel_time(dist, speed): # by hours
    return dist / speed

def calc_travel_time2(dist, speed): # by minutes
    return (dist / speed) * 60

travel_time_hours = calc_travel_time(distance, avg_speed)
travel_time_minutes = calc_travel_time2(distance, avg_speed)
print(f"To get to your destination, the trip will take about {travel_time_hours} hours or {travel_time_minutes} minutes.")

# To answer Question #4, we need to figure out the amount of money the trip would cost me from Answer #1 and the price per gallon cost.
def calc_money_cost(gall, price):
    return price * gall

money_cost = calc_money_cost(full_trip_gall, ppg)
print(f"The cost of your trip should amount to be approximately ${money_cost:.2f}.")

# To answer Question #5, we need to figure out if we can afford the trip from the initial amount of money possessed and Answer #4 and if not, how much more we would need.
def calc_gallons_afford(income, expense):
    return income - expense

gallons_afford = calc_gallons_afford(initial_money, money_cost)
if (gallons_afford > 0):
    print(f"With the money I have and current cost per gallon, I will have ${gallons_afford:.2f} leftover.")
elif (gallons_afford < 0): 
    print(f"With the money I have and current cost per gallon, I need ${gallons_afford:.2f} more.")
else:
    print(f"With the money I have and current cost per gallon, I will just have enough money.")

