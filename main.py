
u1 = 9
u2 = 6
print("I`m thinking of 2 numbers: ")

op = input("Enter + or - : ")
if op == "+":
    print("a + b = ", u1 + u2)
elif op == "-":
    print("a - b = ", u1 - u2)
else:
    print("that`s not a choice.")

op = input("enter + or - : ")
if op == "+":
    print("a + b = ", u1 + u2)
elif op == "-":
    print("a - b = ", u1 - u2)
else:
    print("That`s not a choice.")

a = int(input("Guess a? "))
b = int(input("Guess b? "))

if a == u1 and b == u2:
    print("You guess!")
else:
    print("Nope. Play again!")



n1 = int(input("enter a number: "))

if n1 > 0:
    print("positive")
elif n1 < 0:
    print("negative")
else:
    print("zero")


    
love = True
hate = False

if love and not hate:
    print("happy!")
elif not love and hate:
    print("angry!")


age = int(input("What is you age?"))
year = 2020 - age
if age < 0:
    print("Wrong age")
if age > 100:
    print("wow! no way")
if 0 <= age <= 100:
    print("your were born ", age, " years ago!")
    print("In ", year)

    

name1 = input("What is your name?")
name2 = input("What is you family name?")

space = name1.find(" ")
name1_first = name1[0:space]
name1_last = name1[space+1:len(name1)]
space = name2.find(" ")
name2_first = name2[0:space]
name2_last = name2[space+1:len(name2)]

name1_first_1sthalf = name1_first[0:int(len(name1_first)/2)]
name1_first_2ndhalf = name1_first[int(len(name1_first)/2):len(name1_first)]
name1_last_1sthalf = name1_last[0:int(len(name1_last)/2)]
name1_last_2ndhalf = name1_last[int(len(name1_last)/2):len(name1_last)]

name2_first_1sthalf = name2_first[0:int(len(name2_first)/2)]
name2_first_2ndhalf = name2_first[int(len(name2_first)/2):len(name2_first)]
name2_last_1sthalf = name2_last[0:int(len(name2_last)/2)]
name2_last_2ndhalf = name2_last[int(len(name2_last)/2):len(name2_last)]

new_name1_first = name1_first_1sthalf + name2_first_2ndhalf
new_name1_last = name1_last_1sthalf + name2_last_2ndhalf
new_name2_first = name2_first_1sthalf + name1_first_2ndhalf
new_name2_last = name2_last_1sthalf + name1_last_2ndhalf

print(new_name1_first, new_name1_last)
print(new_name2_first, new_name2_last)



day = input("what day of the week? ")
num = int(input("how may times? "))
print("It`s", day*num)


phrase = "Eak, two snake eyes"
num = "1"

num_repeat = num * 4
print(num_repeat)


minutes_to_convert = 123
hours = int(minutes_to_convert / 60)
minutes = minutes_to_convert % 60

print("Hours")
print(hours)
print("Minutes")
print(minutes)




import datetime
x = datetime.datetime.now()
print ("The date and time: ", x)


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def is_positive(number):
  if number > 0:
    return True
  else:
    return False
is_positive(5)


def convert_distance(miles):
    km = miles * 1.6 # approximately 1.6 km in 1 mile
    return km
kilo_mile = convert_distance(55)
print("The distance in kilometers is",str(kilo_mile))
round_trip = kilo_mile * 2
print("The round-trip in kilometers is",str(round_trip))


def convert_distance(miles):
    return miles * 1.6
miles = convert_distance(55)
km = convert_distance(55*2)
print("The distance in kilometers is: " + str(miles))
print("The round-trip in kilometers is: " + str(km))


def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km
miles = 55
km = convert_distance(miles * 2)
distance = convert_distance(miles)
print("The distance in kilometers is: " + str(distance))
print("The round-trip in kilometers is: " + str(km))



def print_monthly_expense(month, hours):
    time = hours * 0.65
    print("In " + month + " We spent : " + str(int(time)))

print_monthly_expense("June",243)
print_monthly_expense("July",325)
print_monthly_expense("August",298)


def lucky_number(name):
    number = len(name) * 1
    print("Hello! " + name + ". Your lucky_number is " + str(number))

lucky_number("Tanesha")
lucky_number("Tolik")


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(999999)
print(hours, minutes, seconds)


def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " +str(sum))


def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)



sum = 2048 + 4357 + 97658 + 125 + 8
amount = 5
average = sum/amount

print("The average size is: " + str(average))

def print_seconds(hours, minutes, seconds):
    print(seconds)

print_seconds(1,60,3600)


name = "AnatoliiPerfun"
print("Hello  "  + name)

color = "red"
thing = "life"
print(color + " is the color of " + thing)

x = 2
y = 3
a = x + y
print(a)

x = 5**(1/2)
ratio = ((1+x)/2)
print(ratio)



name = "Automating with Python is fun!"
print(name)


color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)


a = 86400
b = 7
c = a*b
print(c)


a = 26
b = (((((a*26)*26)*26)*26)*26)
print(b)


disk_size = (((16*1024)*1024)*1024)
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)
