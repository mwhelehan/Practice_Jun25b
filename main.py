print("Matt is way to tired!")
name = input("What is your name?")
print (f"Nice to meet you {name} .")

weather = input("How is the weather?")
Temperature = input("What is the temperature")

if weather.strip().lower() == "hot":
    print(f"Yes temperature, is {Temperature}")

else:
    print(f"Oh its {weather} today the temp is {Temperature}")

#Numeric Input + Type Conversion
age = "What is your age?"
# this is a string not a number 
age = int(input("how old are you"))
#int makes it a number now
age = int(input("what is your age?"))
if age >= 18:
    print("You are adult")
else:
    print("You are a kid")

#Mini Project: Neon Café Greeter

name = input("Welcome, what is you name?").strip
print(f"Nice to meat you {name}")
weather = input("whats the weather like today").strip().lower()
mood = input ("How are you doing today?").strip().lower()
print(f"yes when the weather is {weather} it makes you feel {mood})")

if weather == "very hot":
    print("can I offer you some iced tea")
elif weather == "warm":
    print("Can I offer you some iced tea")
elif weather == "chilly":
    print("Can I offer you some hot tea")
else:
    print (f"because weather is {weather} what would like today")

