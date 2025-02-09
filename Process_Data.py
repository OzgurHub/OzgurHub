#-----------------------------------------------------------
#------On 10/02/2025 Created by Ozgur Serin,----------------
#------Elizabeth School of London---------------------------
#------Description : Software Foundation Module,------------
# -----Week 4 Python file handling tutorial ----------------
#------Description : How to create excel formulas,----------
#------Week 2 to 7 Computational Reasoning Module ---------
#-----------------------------------------------------------
#------Define the Functions---------------------------------
#----- define average scores by adding up all three scores--
#------then divide it by 3 to get average score-------------
def calculate_average(scores):
    return sum(scores) / len(scores)
#-----------------------------------------------------------
#-----Define the Grades using if elif commands--------------
#-----If above 85 marks, output grade A,--------------------
#-----otherwise output different grade----------------------
#-----either B, or C, or D or F-----------------------------
def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'
#-----End Functions-----------------------------------------
#-----Importing the Student.csv file into Python library----
import csv

#-----Executing the students.csv file list------------------
students = []
#-----------------------------------------------------------
#-----Open the student.csv file and read file---------------
with open('Students.csv', 'r') as file:
        
        #-----Creating a csv reader object------------------
        reader = csv.reader(file)

        #-----Read the headers Name-------------------------
        #-----Art, English, Maths etc (first row)-----------
        header = next(reader)
        
        #-----Extracting field names through first row------
        #-----Calculate the average scores for each student-
        for row in reader:
            name, art, english, maths = row
            average = calculate_average([int(art), int(english), int(maths)])
            grade = assign_grade(average)
            students.append([name, art, english, maths, average, grade])

#-----Create a file named Student_Results.csv----------------------------
# ----Write the results to Student_Results.csv file and open the file----
#-----Data gained from Students.csv 
#-----To calculate the grades in Student_Results.csv Add new headings---- 
#-----Average and Grade into Student_Results.csv file on first row-------
with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Art', 'English', 'Maths', 'Average', 'Grade'])
        writer.writerows(students)

#-----Results are saved under the correct names--------------------------
#-----And subject headings with students marks and grades----------------
#-----Results saved and displayed in Students_Results.csv file-----------
print('Results saved to student_results.csv')
#-----Program coding executes--------------------------------------------
#-----And runs successfully without errors-------------------------------
#-----Program ends and stops executing-----------------------------------