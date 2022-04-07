name=input("What is your name?\n")
print("Nice to meet you, ",name,".",sep="")
import time
time.sleep(1.5)
print(name,", why are you gay?!\n")
time.sleep(1.5)
age = int(input("How old are you, "+name+"?\n"))
time.sleep(1.5)
print("Your name is ",name,". ","You are very gay."," You are currently ",age,".\n",sep="" )

# Eric Lee
# 03/17/2022
# Tool to calculate area of a square
time.sleep(2)
side=int(input("Please enter the side of your square.\n"))
area = side*side
print("The area of a square with side", side,"is",area)

# Eric Lee
# 03/17/2022
# Tool to calculate total price of an item

tax_rate = 6.5
time.sleep(1.5)
print("..."
      "..."
      "..."
      "..."
      "..."
      "...\n")

time.sleep(1.5)
item_price = float(input("Please enter the price of your item.\n"))
total_price = item_price*(1+tax_rate/100)
print("The total price of your item is $",total_price, end="\n")
time.sleep(1)
print("Merry Christmas, you filthy animal!~")
time.sleep(0.5)
print("And a happy new year!")


# Eric Lee
# 03/17/2022
# Program to convert Celsius to Fahrenheit
time.sleep(1.5)
print("..."
      "..."
      "..."
      "..."
      "..."
      "...\n")
temp_cel=float(input("Please enter the temperature in Celsius, por favor.\n"))
temp_fah=(1.8*temp_cel)+32
print(temp_cel,"degrees Celsius is equal to",temp_fah,"degrees Fahrenheit.")


# Eric Lee
# 03/17/2022
# Calculates the number of miles before having to refuel.

time.sleep(1.5)
print("..."
      "..."
      "..."
      "..."
      "..."
      "...\n")

start_odometer = int(input("what is the initial reading on the odometer?\n"))
gas_tank = float(input("How many gallons of gas does your tank hold?\n"))
mid_odometer = int(input("what is the second reading on the odometer?\n"))
gas_left = float(input("How many gallons of gas were left then?\n"))

miles_driven=mid_odometer - start_odometer
gas_used=gas_tank - gas_left

mpg=miles_driven/gas_used
distance_left=gas_left*mpg

print("You can go another",distance_left,"before stopping to refuel.\n")
print("Good luck getting to where you're going, gay boy!!")


time.sleep(1.5)
print("..."
      "..."
      "..."
      "..."
      "..."
      "...\n")

# Eric Lee
# 03/17/2022
# Calculating lemonade stand profitability

rent=int(input("how many dollars is the daily rent, bitch?\n"))
cost=int(input("how many cents is the material that goes into one glass, bitch?\n"))
price=int(input("how many cents is one glass of your sweet lemonade, delicious?"))
profit_goal=int(input("how much do you wanna make as your profit from this hustle?\n"))

profit_per_cup = price - cost

target = 100*(rent+profit_goal)



