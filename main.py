
def read_file(file):
    
    
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n","")
        if line_count % 2 == 0:
             first_every_2 += (stripped_line, )
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line, )
        line_count += 1
        
    return (first_every_2, second_every_2)
    
def sanitize(some_tuple):
    
    clean_string = ()
    for st in some_tuple:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace(")", "")
        st = st.replace("(", "")
        clean_string += (st, )
    return clean_string     

def analyze_friends(names, phones, all_areacodes, all_places):
    
    
    def get_unique_area_codes():
        
        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:
               area_codes += (ph[0:3], ) 
        return area_codes

    def get_states(some_areacodes):
        
        states = ()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states += ("bad areacode", )
            else:
                index = all_areacodes.index(ac)
                states += (all_places[index], )
        return states 

    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)
    
    print("You have", num_friends, "Friends!")
    print("They live in: ")
    for s in unique_states:
        print(s)
        
friends_file = open("phone.txt")
map_file = open("adress.txt")
(names, phones) = read_file(friends_file)
(areacodes,places) = read_file(map_file)
friends_file.close()
map_file.close()
clean_phones = sanitize(phones)
analyze_friends(names, clean_phones, areacodes, places)
# print(names)
# print(clean_phones)




def normalize_to_100(score, out_of):
    
    return score*100/out_of
def pass_or_fail(score, out_of):
    
    if normalize_to_100(score, out_of) > 50:
        return "pass"
    else:
        return "fail"
        
def grade(student_scores, out_of, f):

    for i in student_scores:
        print(i[0], ":", f(i[1], out_of))
        
scores = (("ana", 7.5), ("pavel", 8), ("dima", 4.8))       
grade(scores, 10, pass_or_fail)





def sandwich(kind_of_sandwich):
    print("-------")
    print(kind_of_sandwich())
    print("-------")
    
def blt():
    my_blt = "bacon\nlettuce\ntomato"
    return my_blt

def breakfast():
    my_ec = "egg\ncheese\negg"
    return my_ec
    
sandwich(blt)
sandwich(breakfast)



def sing():
    def stop(line):
        print("stop",line)
    stop("mazafaka") 
    stop("pipipi")
    stop("wowowow")

sing()




def seat_at_tables(group):
    big_table = 3
    big_fit = 6
    small_table = 3
    small_fit = 4
    
    possible = ()
    
    for i in range(big_table + 1):
        for j in range(small_table + 1):
            possible += (i*big_fit + j*small_fit,  )
    return group in possible

print(seat_at_tables(11))        
    



def get_full_length(words):
    
    length = 0
    for word in words:
        length += len(word)
        return length  
w = ("hello", "it is", "me") 
print(get_full_length(w))





words = """ art
bolt
drop
mail
hat
dog
cat
math
pan
but
on
at
not
or
are
next
left
right
well
good
fine
inside
outside
back
white
yellow
low
fast
break
after
mama
papa
sister
brother
need
down
sun
water
sand
seed
plain
tank
car
  """
 
all_valid_words = ()
start = 0
end = 0

for char in words:
    if char == '\n':
        all_valid_words = all_valid_words + (words[start:end], )
        start = end + 1
        end = end + 1
    
    else:
        end = end + 1
tiles = input("type any letters: ")        
found_words = ()

for word in all_valid_words:
    all_letters_in_word = True
    tiles_left = tiles 
     
    for letter in word:
        
        if letter not in tiles_left:
            all_letters_in_word = False
            break
        
        else:
            index = tiles_left.find(letter)
            tiles_left = tiles_left[0:index] + tiles_left[index+1:len(tiles_left)]
        

    if all_letters_in_word:
        found_words = found_words + (word, )
        
for w in found_words:
    print(w)
     
print(found_words)        

    


while True:
    pwd = input("Create a password: ")
    longer_than_6 = (len(pwd) >= 6)
    has_capital = False
    has_digits = False
    for ch in pwd:
        if ch in "0123456789":
            has_digits = True
        if ch in "QWERTYUIOPASDFGHJKLZXCVBNM":
            has_capital = True
    if not longer_than_6:
        print("Must be 6 or more characters")
    if not has_digits:
        print("Must have at least one digit")
    if not has_capital:
        print("Must have at least one capital letter")
        
        
    if not longer_than_6 or not has_digits or not has_capital:
        continue
    break
print("Password have been created!")





for i in range(1, 11):
    if i%3 == 0:
        continue
    print(i)



for i in range(5):
    print("in for loop", i)
    
    i = 0
while i < 5:
    print("in while loop", i)    
    i += 1


text = input("Wash? YES or NO:")

while text == "YES":
    print("Rinse")
    text = input("wash again? YES or NO")
    


n = int(input("What is hight of your triangle?:"))

for i in range(1, n+1):
    print("*" * i)
    
for i in range(n-1, 0, -1):
    print("*" * i)
  



print("You`re on Island in a dark cave!")
print("Try to survive until rescue arrives!")
print("Rules: ")
print("All available commands are in CAPITAL LETTERS.")
print("Any other command wxits the program.")
text = input("First LOOK around...")
if text == "LOOK":
    text = input("LEFT you hear rustling. RIGHT you see a light.")
    if text == "LEFT":
        print("A snake bites you! You are dead =(")
    elif text == "RIGHT":
        text = int(input("How many steps will you walk? "))
        if text == 0:
            print("You stay and miss the rescue plane =(")
        elif text < 10:
            text = input("You see BERRIES and LEAVES to eat:")
            if text == "BERRIES":
                text = input("EAT them or NOT?")
                if text == "EAT":
                    print("Should not have. They make you sick =(")
                elif text == "NOT":
                   text = input(
                       "You spot a plane! make a FIRE or run to a CLEARING? ")
                   if text == "FIRE":
                       print("You took too long =(")
                   elif text == "CLEARING":
                       print("They see you. You`re saved!!!")
                   else:
                           print("Only type in commmads in CAPITAL LETTERS.")
                else:
                    print("Only type in commmads in CAPITAL LETTERS.")

            elif text == "LEAVES":
               text = input("Boil them with OCEAN water or PUDDLE water?")
               if text == "OCEAN":
                   print("A little solty, but ok. You stay hydrated and live!")
               elif text == "PUDDLE":
                   print("You fall ill, and miss the rescue plain!=(")
               else:
                   print("Only type in commmads in CAPITAL LETTERS.")
            else:
                print("Only type in commands in CAPITAL LETTERS!")

        elif text >= 10:
            print("You walked off a cliff =(")

        else:
            print("You didn`t follow the commands.")

    else:
        print("Only type in commands in CAPITAL LETTERS!")
else:
    print("Only type in commands in CAPITAL LETTERS!")



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
