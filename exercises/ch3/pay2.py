try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours < 40:
        pay = hours * rate
    elif hours > 40:
        extra_hours = hours-40
        pay = (40 * rate) + (extra_hours * (1.5*(rate)))

    print("Pay:", pay)
except:
    print("Must be a number")


