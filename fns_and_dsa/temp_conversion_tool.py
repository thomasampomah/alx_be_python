FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

temperature = float(input("Enter the temperature to convert: "))

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR

convert_to_celsius(temperature)


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR

convert_to_fahrenheit(temperature)

if unit == "F":
        print(f"{temperature} °F  is {FAHRENHEIT_TO_CELSIUS_FACTOR} °C ")

elif unit == "C":
        print(f"{temperature} °C is {CELSIUS_TO_FAHRENHEIT_FACTOR} °F")

else:
      print("Invalid temperature. Please enter a numeric value.")