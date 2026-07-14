import matplotlib.pyplot as plt

x = [1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y,color="green",marker="o",linestyle="--")

plt.title("student marks")
plt.xlabel("student")
plt.ylabel("marks")

x= ["charvi","aman","riya","manas","kritvi"]
y= [99,98,97,100,89]
plt.bar(x,y,
        color=["blue","green","purple","pink","orange"],
        edgecolor="brown",
        width=0.5)
plt.title("student marks")
plt.xlabel("student")
plt.ylabel("marks")


course=["AI","python","ML","DSA"]
students=[20,31,23,17]
plt.pie(students,labels=course,colors=["blue","green","orange","pink"],autopct="%1.1f%%",explode=[0.2,0,0,0])
plt.title("student in courses")

age = [20,21,22,19,20]
marks = [88,98,97,78,89]
plt.scatter(age,marks)
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.show()



# marks = [45, 50, 52, 55, 60, 61, 62, 70, 72, 75, 80, 82, 90, 95]

# plt.hist(marks)

# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.grid(color="blue")
# plt.show()

# x =[1,2,3,4]

# marks1 = [80,87,90,95]
# marks2 = [78,86,97,88]

# plt.figure(figsize=(8,5))
# plt.plot(x , marks1 , label="chaarvi",color="blue",marker="o")
# plt.plot(x , marks2 , label="riya",color="pink",marker="o")

# plt.grid()
# plt.title("marks comparison")
# plt.xlabel("test")
# plt.ylabel("marks")

# plt.legend()
# plt.show()





