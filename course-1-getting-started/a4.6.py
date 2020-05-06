# compute the pay using hours and rate
def computepay(hrs, rate):
    if hrs > 40:
        pay = (hrs - 40) * rate * 1.5 + (40 * rate)
    else:
        pay = hrs * rate
    return pay


hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = computepay(hrs, rate)
print("Pay", pay)
