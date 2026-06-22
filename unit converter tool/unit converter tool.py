print("===== UNIT CONVERTER =====")

print("1. Kilometer to Meter")
print("2. Kilogram to Gram")
print("3. Celsius to Fahrenheit")

choice = int(input("Enter Choice: "))

if choice == 1:
    km = float(input("Enter Kilometer: "))
    print("Meter =", km * 1000)

elif choice == 2:
    kg = float(input("Enter Kilogram: "))
    print("Gram =", kg * 1000)

elif choice == 3:
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit =", f)

else:
    print("Invalid Choice")