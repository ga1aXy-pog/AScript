age = None
while age is None:
    input_value = input("Please enter your age: ")
    try:
        # try and convert the string input to a number
        age = int(input_value)
    except ValueError:
        # tell the user off
        print("{input} is not a number, please enter a number only".format(input=input_value))

name1 = "Rithwik"

while True:
    name = input("Enter your name: ")
    if name == name1:
        print('')
        break
    else:
        continue



bday = '28th'

while True:
    user = input('when is your bday?:')
    if user == bday:
        print('')
        break
    else:
        continue





from datetime import datetime
# Returns a datetime object containing the local date and time
dateTimeObj = datetime.now()
print(dateTimeObj)


import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
print(now.hour, now.minute) # continous change when the local time changes
time = now.hour, now.minute


if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good night"

print("{}!".format(greeting + "\n" + name + "\nYour local time is shown above"))

number = 2
 
