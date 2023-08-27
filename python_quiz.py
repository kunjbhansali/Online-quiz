# --------------------------------------- Importing Modules -----------------------------------------
import matplotlib.pyplot as plt
import pymysql


# --------------------------------------- Establishing Connections ---------------------------------
global conn
global cursor

conn = pymysql.connect(host="localhost",user="root",passwd="root",db="onlineexm")
cursor = conn.cursor()


# -------------------------------------- SUPERVISOR SECTION ----------------------------------------
class sup:
    # 1. Adding Question
    def sup_addQues(self):
        qno = 'select count(*) from exam'
        cursor.execute(qno)
        qn = int(cursor.fetchone()[0])+1
        while (True):
            q = input("Enter question: \n")
            a = input("Enter option 1: ")
            b = input("Enter option 2: ")
            c = input("Enter option 3: ")
            d = input("Enter option 4: ")
            ca = int(input("Enter correct ans[1/2/3/4]: "))
            sql = f"""insert into exam(Questionnumber, Question,optionA,optionB,optionC,optionD,correctans)
                    values({qn}, '{q}', '{a}', '{b}', '{c}', '{d}', {ca})"""
            cursor.execute(sql)
            qn += 1
            opt = input("Do you want to add another question[y/n]? : ")
            if (opt.lower() == 'y'):
                continue
            else:
                break
        conn.commit()

    # 2. Deleting Question
    def sup_delQues(self):
        qn = int(input("Enter question Number to be deleted "))
        delq = f"delete from exam where Questionnumber = {qn}"
        cursor.execute(delq)
        upq = f"update exam set Questionnumber = Questionnumber-1 where Questionnumber > {qn}"
        cursor.execute(upq)
        conn.commit()
        
    # 3. Displaying Report
    def sup_seeReport(self):
        sr1 = "select * from marks"
        cursor.execute(sr1)
        rep = cursor.fetchall()
        for i in rep:
            print ("\n")
            sr2 = f"select * from student_details where RollNo = {i[0]}"
            cursor.execute(sr2)
            det = cursor.fetchone()
            print ("Roll Number:\t", det[0])
            print ("Name:\t\t", det[1])
            print ("Class:\t\t", det[2])
            print ("Mobile No.:\t", det[3])
            print ("Email ID:\t", det[4])
            print ("Right Attempts: ", i[1])
            print ("Wrong Attempts: ", i[2])
            print ("Skipped:\t", i[3])
            print ("Total Score:\t", i[4])
            print ("\n")

    # -------------------------------- Main Function For Supervisor -------------------------------------
    def supervisor(self, sid, password, operation):
        sql = f"select password from supervisor where id = {sid}"
        cursor.execute(sql)
        pas = cursor.fetchone()
        if (pas == None):
            print ("\nNo record exist\n")
        else:
            if (password == pas[0]):
                if (operation == 1):
                    self.sup_addQues()
                elif (operation == 2):
                    self.sup_delQues()
                else:
                    self.sup_seeReport()
            else:
                print ("\nIncorrect Password\n")




# ---------------------------------------- CANDIDATE SECTION -------------------------------------------------
class student:
    # ----------------------------------- Variables -------------------------------------------------
    RQ = WQ = SK = total_score = None

    # ----------------------------------- Constructor ------------------------------------------------
    def __init__(self):
        self.RQ = 0
        self.WQ = 0
        self.SK = 0
        self.total_score = 0

    # ---------------------------------- Student Details ----------------------------------------------
    def sd(self, rollNo):
        NAME=input("ENTER YOUR NAME ")
        CLASS=input("ENTER YOUR CLASS ")
        MOBNO=int(input("ENTER YOUR MOBNO "))
        GMAIL=input("ENTER YOUR EMAILID ")
        det = f"insert into student_details values ({rollNo}, '{NAME}', '{CLASS}', {MOBNO}, '{GMAIL}')"
        cursor.execute(det)
        conn.commit()


    # --------------------------------- Updating record ----------------------------------------------
    def update(self, ROLLNO):
        en = f"insert into marks values({ROLLNO} , {self.RQ}, {self.WQ}, {self.SK}, {self.total_score})"
        cursor.execute(en)
        conn.commit()
        
    
    # --------------------------------- Test Section -------------------------------------------------
    def quesDisplay(self, rollNo):
        tol="select count(*) from exam"
        cursor.execute(tol)
        row=cursor.fetchone()[0]
        for i in range(1,int(row)+1):
            sq=f"select Questionnumber,Question from exam where Questionnumber = {i}"
            cursor.execute(sq)
            row=cursor.fetchone()
            print ("Q", end = "")
            for j in row:
                print (j, end = " ")
            print ("\n")    
                    
            op = f"select optionA,optionB,optionC,optionD from exam where Questionnumber = {i}"
            cursor.execute(op)
            row=cursor.fetchone()
            for j in range(4):
                print ("Option ", j+1, ". ", row[j])
            print ("\n")
            
            choosedans=int(input('Enter your answer: '))
            option=[1,2,3,4]
            can=f"select correctans from exam where Questionnumber = {i}"
            cursor.execute(can)
            chans = cursor.fetchone()[0]
            
            if choosedans==chans:
                self.RQ+=1
                
            elif choosedans in option:
                self.WQ+=1
            
            else:
                self.SK+=1

        self.total_score = self.RQ*4 - self.WQ*1
        self.update(rollNo)


    # ------------------------------------- Main student section --------------------------------------
    def stud(self):
        rn = int(input("ENTER YOUR ROLLNO "))
        self.sd(rn)
        self.quesDisplay(rn)


    # ------------------------------------- Your Response ---------------------------------------------
    def response(self):
        print ("\n" + "+"*40 + "YOUR SCORE" + "+"*40)
        print ("Right Answers:",self.RQ,"\nWrong Answers:",self.WQ,"\nSkipped",self.SK,"\n--------------\nTotal marks",self.total_score)
        labels = 'CORRECT ANS', 'WRONG ANS','SKIPPED'
        sizes = [self.RQ,self.WQ,self.SK]
        colors = ['gold', 'yellowgreen',"red"]
        plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title("REPORT")
        plt.axis('equal')
        plt.show()




# --------------------------------------------- Main --------------------------------------------------
opt=input( "Are you supervisor[y/n]? ")
if (opt.lower() == 'y'):
    s1 = sup()
    sid = int(input("Enter your ID: "))
    pwd = input("Enter password: ")
    oper = int(input("Enter operation: "))
    s1.supervisor(sid, pwd, oper)

else:
    c1 = student()    
    c1.stud()
    rep = input("Do you want to see your report[y/n]? ")
    if (rep.lower() == 'y'):
        c1.response()
    



# -------------------------------------- Closing Connections ------------------------------------------
cursor.close()
conn.close()
