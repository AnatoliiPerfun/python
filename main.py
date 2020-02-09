
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
