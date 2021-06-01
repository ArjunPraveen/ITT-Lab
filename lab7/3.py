import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute('''CREATE TABLE STUDENT
 (STUDENtID INT PRIMARY KEY NOT NULL,
 REGNO INT NOT NULL,
 NAME TEXT NOT NULL,
 SEMESTER INT NOT NULL,
 BRANCH CHAR(50) NOT NULL,
 CGPA INT NOT NULL,
 EMAIL TEXT);''')
print ("Table created successfully")

conn.execute("INSERT INTO STUDENT (STUDENTID, REGNO, NAME, SEMESTER,BRANCH, CGPA, EMAIL) VALUES (1, 180911230, 'ARJUN', 5, 'IT', 10, 'a@gmail.com')")
conn.execute("INSERT INTO STUDENT (STUDENTID, REGNO, NAME, SEMESTER,BRANCH, CGPA, EMAIL) VALUES (2, 180911220, 'RAM', 5, 'CSE', 5, 'r@gmail.com' )")
conn.execute("INSERT INTO STUDENT (STUDENTID, REGNO, NAME, SEMESTER,BRANCH, CGPA, EMAIL) VALUES (3, 180911110, 'SHYAM', 5, 'CCE', 8, 's@gmail.com')")
conn.execute("INSERT INTO STUDENT (STUDENTID, REGNO, NAME, SEMESTER,BRANCH, CGPA, EMAIL) VALUES (4, 180911010, 'SAM', 5, 'IT', 9,'s1@gmail.com' )")
conn.commit()

print("\nSearching for student with registration number = 180911230")
cursor = conn.execute("SELECT studentid, name, regno, branch from STUDENT where regno = 180911230")
for i in cursor:
    print("StudentID: " + str(i[0]))
    print("Name: " + i[1])
    print("RegNo: " + str(i[2]))
    print("Branch: " + i[3])
conn.close()