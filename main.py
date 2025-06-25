print("Matt is way to tired!")
name = input("What is your name?")
print (f"Nice to meet you {name} .")

weather = input("How is the weather?")
Temperature = input("What is the temperature")

if weather.strip().lower() == "hot":
    print(f"Yes temperature, is {Temperature}")

else:
    print(f"Oh its {weather} today the temp is {Temperature}")