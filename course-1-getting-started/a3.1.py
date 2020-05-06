# take hours and rate from the user
hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# calculate and show the pay
if hrs > 40:
    pay = (hrs - 40) * rate * 1.5 + (40 * rate)
else:
    pay = hrs * rate
print(pay)
