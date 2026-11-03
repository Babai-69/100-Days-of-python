# Write a function named calculate_grade(marks,full_marks).

# Requirements:
# 1. Ask the user to enter their marks (out of 100).
# 2. Create a function named calculate_grade(marks). [>20%= FAIL][20%-30%=F],[30%-40%=P],[40%-50%=D],[50%-60%=C],[60%-70%=B],[70%-80%=A],[90%-100%=E],[90-100=O]
# 3. Use if-elif-else to calculate the grade.
# 4. Return the grade.
# 5. Handle invalid marks (less than 0 or greater than 100).

def calculate_grade(x,y):

    if x < 0 or x > y or y <= 0:
        return "Invalid marks!"
        
    percentage=(x/y)*100

    if percentage<=20:
            return("You are FAIL and will not be upgraded to next class!")
    elif 20<percentage<=30:
            return("F")
    elif 30<percentage<=40:
            return("P")
    elif 40<percentage<=50:
            return("D")
    elif 50<percentage<=60:
            return("C")
    elif 60<percentage<=70:
            return("B")
    elif 70<percentage<=80:
            return("A")
    elif 80<percentage<=90:
            return("E")
    elif 90<percentage<=100:
            return("O")
    else:
            return("Please enter the marks!")

marks=int(input("Marks= "))
print("Marks= ",marks)
full_marks=int(input("Enter the Full Mark= "))
print("Full Mark= ",full_marks)

grade=calculate_grade(marks,full_marks)
print("Grade is: ",grade)