age=int(input("Enter the age for blood donation:"))
weight=float(input("enter the weight in kg:"))
if age>=18:
    if age<=65:
        if weight>=50:
            print("You are eligible to donate blood")
        else:
            print("You are not eligible to donate blood")

    else:
        print("You are not eligible to donate blood due to insufficient weight")

else:
    print("You are not eligible due to age restrictions or age limit")
   