number = 0
sum = 0
while (number < 5):
   number =  number + 1
   feedback = int(input ("enter " + str(number) + " feedback rate:"))
   sum = sum+feedback
avg = sum/5
print("average feedback is:", avg)

if (avg > 4):

    print("ver good")
elif (avg > 3):
    print("good")
elif (avg > 2):
    print("average")
else:
    print("bad")