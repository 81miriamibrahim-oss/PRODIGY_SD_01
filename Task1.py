
unit = input ("Is the temperature in Celsius or Fahrenheit or Kelvin (C/F/K): ")
temperature = float(input("Enter the temperature value: "))

if unit.upper() == "C":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin}K.")
elif unit.upper() == "F":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temperature}°F is equal to {celsius}°C and {kelvin}K.")
elif unit.upper() == "K":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temperature}K is equal to {celsius}°C and {fahrenheit}°F.")
else:
    print("Invalid unit. Please enter C, F, or K.")
