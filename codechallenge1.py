# grade of a student

sub1 = 98
sub2 = 89
sub3 = 100
sub4 = 95
sub5 = 79
print("__score card__")
total = sub1+sub2+sub3+sub4+sub5
perc = (total / 500) * 100
print("Total Marks = ",total,"/500")
print("Percentage = ",perc)
if perc >= 90 and perc <= 100 :
    print("Grade = A+")
elif perc >= 80 and perc < 90 :
    print("Grade = A")
elif perc >= 70 and perc < 80 :
    print("Grade = B")
elif perc >= 60 and perc < 70 :
    print("Grade = C")
elif perc >= 50 and perc < 60 :
    print("Grade = D")
elif perc < 50 :
    print("Grade = F")
else:
    print("check marks")
