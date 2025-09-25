# create a list of first 100 numbers
# from that list create lists for :
# all even numbers, all odd numbers, numbers that divisible by both 5 and 3
list=[]
even_list = []
odd_list = []
div_list = []

for i in range(1,101):
    list.append(i)
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
    if i % 5 == 0 and i % 3 == 0 :
        div_list.append(i)
print("list :",list,"\n")
print("list of even numbers :",even_list,"\n")
print("list of odd numbers :",odd_list,"\n")
print("list of numbers div by 3 and 5 :",div_list)