print(" ")
print("   ---------   ###### EXERCISE 38 ##########   ---------   ")
print(" ")
# Page 169

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait ther are not 10 thing in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)}  items now")

print("There we go:", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
print('Normal:: ', stuff)
print('Inverse::', stuff[::-1])
