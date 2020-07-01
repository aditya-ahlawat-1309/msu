hrs = float(input("Enter Hours:"))

rate = float(input("Enter rate:"))
if hrs>40 :
  print(40*rate + (hrs-40)*1.5*rate)
else :
    print(hrs*rate)