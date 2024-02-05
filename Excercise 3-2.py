hw = input("Enter Hours: ")
hr = input("Enter Rate: ")
try:
    fh = float(hw)
    fr = float(hr)
except:
    print("Error, Please enter a number value")
    quit()
print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    tp = reg + otp
else:
    tp = fh * fr
print("Pay:",tp)