def computepay(hours, rate) :
    # print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

hw = input("Enter Hours: ")
hr = input("Enter Rate: ")
fh = float(hw)
fr = float(hr)
# print(fh, fr)
tp = computepay(fh,fr)

print("Pay:",tp)