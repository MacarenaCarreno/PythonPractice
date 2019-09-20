print(" ")
print("   ---------   ###### EXERCISE 12 ##########   ---------   ")
print(" ")
print("Practicing print!")
print("Hello Word!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay!! Printing.')
print("I'd much rather you 'not'.")
print('I "Say" do not touch this.')

print(" ")
print("   ---------   ###### EXERCISE 2 ##########   ---------   ")
print(" ")
print("Practicing the # Octothorpe")
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print("I couldh have code like this.") # and the comment after is ignored
# You can also use a comment to "disable" or comment out code:
# print("This won't run")

print("This will run.")



print(" ")
print("   ---------   ###### EXERCISE 3 ##########   ---------   ")
print(" ")

print("I will now count my chickens:")
print("Hens", 25+30/6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3+2+1-5+4%2-1/4+6)
print("Is it true that 3+2 < 5-7??")
print(3+2 < 5-2)

print('What is 3+2?', 3+2)
print('What is 5-7?', 5-7)
print("Oh, that's why it's false")

print("How about some more.")

print("Is it greater?", 5>-2)
print("It is greater or equal?", 5 >= -2)
print("It is less or equal?", 5<= -2)


print(" ")
print("   ---------   ###### EXERCISE 4 ##########   ---------   ")
print(" ")

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_pasengers_per_car = passengers / cars_driven

print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers available.")
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_pasengers_per_car, 'in each car.')

print('Check Equal', cars == drivers)
print('Check Equal', cars == passengers+10)


print(" ")
print("   ---------   ###### EXERCISE 5 ##########   ---------   ")
print(" ")

myName = 'Zed A. Shaw'
myAge = 35
myHeight = 74
myWeight = 180
myEyes = 'Brown'
myTeeth = 'White'
myHair = 'Purple'

print(f"Let's talk about {myName}.")
print(f"He's {myHeight} inches tall.")
print(f"He's {myWeight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {myEyes} eyes and {myHair} hair. ")
print(f"His teeth are usually {myTeeth} depending on the coffee.")

#This line is tricky...

total = myAge + myHeight + myWeight

print(f"If I add {myAge}, {myHeight}, and {myWeight} I get {total}, ")

myHeightInCm= myHeight * 2.54

print(f"His hight in centimeters is {myHeightInCm}")



print(" ")
print("   ---------   ###### EXERCISE 6 ##########   ---------   ")
print(" ")

types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f'I said: {x}')
print(f"I also said:'{y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


print(" ")
print("   ---------   ###### EXERCISE 7 ##########   ---------   ")
print(" ")

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And eveywhere that Mary went.")
print("."*10)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)


print(" ")
print("   ---------   ###### EXERCISE 8 ##########   ---------   ")
print(" ")

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your", 
  "the best is fresh",
  "local delivery",
  "grocery brancs delivered to your door"
))



print(" ")
print("   ---------   ###### EXERCISE 9 ##########   ---------   ")
print(" ")

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nAbr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
print("Here are the days: ", days)
print("Here are the Months", months)
print("""
  There is something going on there.
  With the three double-quotes.
  We'll be able to type as much as we like.
  Even 4 lines if we want, or 5, or 6.
  This is the 5.
""")


print(" ")
print("   ---------   ###### EXERCISE 10 ##########   ---------   ")
print(" ")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t*Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


print(" ")
print("   ---------   ###### EXERCISE 11 ##########   ---------   ")
print(" ")

# print("How old are you?", end = ' ')
# age = input()
# print("How tall are you?", end = ' ')
# height = input()
# print("How much do you weigh?", end = ' ')
# weight = input()

# print(f"So, you'r {age} old, {height} tall and {weight} heavy.")


print(" ")
print("   ---------   ###### EXERCISE 12 ##########   ---------   ")
print(" ")

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weight? ")

# print(f"So, you are {age} old, {height} tall and {weight} heavy.")

