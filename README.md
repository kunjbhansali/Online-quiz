# Online-quiz

It is basically a python project aimed to conduct online mcq based test.

# Libraries used
1. PyMySQL
2. matplotlib.pyplot

# Lib1: PyMySQL
It connects python with MySQL.
Operations written in python can be executed in MySQL to get data and maintain records.

# Tables used in MySQL
1. Supervisor table: It is used to maintain supervisor records and their ID-passwords for different changes to be made in exam table.
2. Exam table: It contains details about questions and answers along with its 4 options.
3. Student_details table: It is used to maintain the records of students who had given their exams.
4. Marks table: It records the reports of students who had given their exams.

# Lib2: matplotlib.pyplot
It is a library that contains different types of graphs.
Graph that I used here is pie chart.
  -> Pie chart here has the following three entries: 
      1. Right Answer
      2. Wrong Answer
      3. Number of questions skipped.

# Code
Code contains three sections: 
1. Supervisor Section
2. Candidate Section
3. Main Section

# 1. Supervisor Section
-> It has three operations that a supervisor can perform.
-> But before that supervisor has to enter his ID and Password and if the ID exists and password is correct then only he can proceed.
-> Now a supervisor can either:
        1. Add a question
        2. Delete a question
        3. See Reports of Candidates

# 2. Candidate Section
-> In this section one can give exam.
-> First he/she has to enter some of the information, then a candidate can proceed to give the exam.
-> After giving exam, if he wants to see his score than he can see the report.

# 3. Main Section
-> It handles and checks if the user is supervisor or student and then acts accordingly.
