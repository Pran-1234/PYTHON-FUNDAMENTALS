total = int(input("enter the maximum mark of a subject:"))
sub1 = int(input("enter the marks of subject1:"))
sub2 = int(input("enter the marks of subject2:"))
sub3 = int(input("enter the marks of subject3:"))
sub4 = int(input("enter the marks of subject4:"))
sub5 = int(input("enter the marks of subject5:"))

average=(sub1+sub2+sub3+sub4+sub5)/5
print("Average is:",average)
percentage=(average/total)*100
print("according to the percentage ,")
if percentage>90:
    print("Grade:A")
elif percentage>80 and percentage<90:
    print("grade:B")
elif percentage>70 and percentage<80:
    print("Grade:C")
elif percentage>60 and percentage<70:
    print("Grade: D")
else:
    print("Grade:E")