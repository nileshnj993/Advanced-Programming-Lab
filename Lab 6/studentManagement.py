import sqlite3

def studentDB():
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student
    (ID INT PRIMARY KEY NOT NULL, 
    Name TEXT NOT NULL,
    Gender TEXT,
    Classroom TEXT, 
    Marks INT);''')
    connection.commit()
    connection.close()

def addStudent(ID, name, gender, classroom, marks):
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO student VALUES (?,?,?,?,?)", (ID, name,gender,classroom,marks))
    connection.commit()
    connection.close()

def dispStudents():
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    print(rows)
    print("\n")
    connection.close()

def deleteStudent(ID):
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM student WHERE ID=?",(ID,)) # add comma at end
    connection.commit()
    connection.close()

def searchStudent(ID):
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM student WHERE ID=?",(ID,))
    rows = cur.fetchall()
    print(rows)
    print("\n")
    connection.close()

def topper():
    connection = sqlite3.connect("student.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM student where Marks in (select MAX(Marks) from student)")
    rows = cur.fetchall()
    print(rows)
    print("\n")
    connection.close()

studentDB()

print('WELCOME TO STUDENT MANAGEMENT SYSTEM!')
print('-------------------------------------')
print("\n")

choice = 0
while(choice!=6):
    print('1. Add new student\n2. View all students\n3. Delete student record\n4. Search for student\n5. Highest Scorer\n6. Exit\n')
    choice = int(input('Please choose:'))
    print("\n")
    if(choice==1):
        ID = int(input('Enter ID:'))
        name = input('Enter Name:')
        gender = input("Enter Gender:")
        classroom = input("Enter Class:")
        marks = int(input("Enter Marks:"))
        addStudent(ID,name,gender,classroom,marks)

    if(choice==2):
        dispStudents()
    
    if(choice==3):
        ID = int(input("Enter ID of student to be deleted: "))
        deleteStudent(ID)
    
    if(choice==4):
        ID = int(input("Enter ID of student to be searched: "))
        searchStudent(ID)
    if(choice==5):
        topper()