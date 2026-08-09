#find the smallest numeber and secomd smallest number in a list
n=list(map(int, input("enter the 10 numbers: ").split()))
n.sort()
print("The smallest number is: ", n[0])
print("The second smallest number is: ", n[1])
#find the largest number and second largest number in a list
n.sort(reverse=True)
print("The largest number is: ", n[0])
print("The second largest number is: ", n[1])
even=[]
odd=[]
if len(n)>0:
    for i in n[:10]:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
print("Even numbers: ", even)
print("Odd numbers: ", odd)
print("the largest even number is: ", max(even))
print("the largest odd number is: ", max(odd))
print("the smallest even number is: ", min(even))   
print("the smallest odd number is: ", min(odd))
print("the second largest even number is: ", sorted(even, reverse=True)[1])
print("the second largest odd number is: ", sorted(odd, reverse=True)[1])