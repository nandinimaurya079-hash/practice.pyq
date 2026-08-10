marks=[]
for i in range(5):
    mark=int(input("Enter marks: "))
    marks.append(mark)
print("Marks of 1 students all subjects:", marks)
marks.sort()
print("highest:",marks[-1])
print("lowest:",marks[0])
average=sum(marks)/len(marks)
print("average:",average)
print("passing subjects",len([i for i in marks if i>=40]))
print("failing subjects",len([i for i in marks if i<40]))

if average>=80:
    print("Excellent")
elif average>=60:
    print("Good")
elif average>=40:
    print("pass")
else:
    print("fail")

        







