hw = input("Enter Hours: ")
hr = input("Enter Rate: ")
fh = float(hw)
fr = float(hr)
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    tp = reg + otp
else:
    # print("Regular")
    tp = fh * fr
#tp = float(hw) * float(hr)
print("Pay:",tp)