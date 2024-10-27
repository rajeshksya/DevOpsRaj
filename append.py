studentCount=0
sum=0
names=[]
feedbacks=[]
while(studentCount<5):
    studentCount=studentCount+1
    name=input("enter the student name")
    names.append(name)
    feedback=int(input("enter the feedback"))
    feedbacks.append(feedback)
    sum=sum+feedback
avg = sum/5
if (avg > 4):

    print("ver good")
elif (avg > 3):
    print("good")
elif (avg > 2):
    print("average")
else:
    print("bad")
print("---feedack of the students---")
for index in range(0,5):
    print("name of the student", names[index])
    print("feedback given by that student", feedbacks[index])


