#loop exercise 16
rain = str(input("Is it raining out? "))
rain = rain.lower()
if rain == "yes":
    wind = str(input("Is it windy? "))
    wind = wind.lower()
    if wind == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")
