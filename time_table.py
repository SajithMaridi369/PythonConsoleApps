0#Class to store the default time tables of all sections
class tables:
    table_sec1=[["CD", "DAA", "ES-1", "DMA", "DMA","DMA"],
                ["AI", "DAA", "DMA", "AECS", "AECS", "AECS"],
                ["DMA", "DAA", "WT", "AI", "AI", "AI"],
                ["WT", "CD", "AI", "WT", "WT", "WT"],
                ["DAA", "DMA", "AI", "WT", "CD", "LIB"],
                ["ES","CD","WT","AI","DMA","DAA"]]
    table_sec2=[["AI", "CD", "DAA", "WT", "WT", "WT"],
                ["ES", "DAA", "WT", "AI", "AI", "AI"],
                ["CD", "WT", "AI", "DMA", "DMA","DMA"],
                ["WT", "DAA", "DMA", "AECS", "AECS", "AECS"],
                ["ES","CD","WT","AI","DMA","DAA"],
                ["DAA", "DMA", "AI", "WT", "CD", "LIB"]]
    table_sec3=[["CD", "DAA", "ES-1", "DMA", "DMA","DMA"],
                ["AI", "DAA", "DMA", "AECS", "AECS", "AECS"],
                ["DMA", "DAA", "WT", "AI", "AI", "AI"],
                ["WT", "CD", "AI", "WT", "WT", "WT"],
                ["DAA", "DMA", "AI", "WT", "CD", "LIB"],
                ["ES","CD","WT","AI","DMA","DAA"]]
    table_sec4=[["AI", "CD", "DAA", "WT", "WT", "WT"],
                ["ES", "DAA", "WT", "AI", "AI", "AI"],
                ["CD", "WT", "AI", "DMA", "DMA","DMA"],
                ["WT", "DAA", "DMA", "AECS", "AECS", "AECS"],
                ["ES","CD","WT","AI","DMA","DAA"],
                ["DAA", "DMA", "AI", "WT", "CD", "LIB"]]
    #Function to print the requested time table
    def print_tb(self,section):
        print("First Period","Second Period","Third Period","Luch Break","Fourth Period","Fifth Period","Sixth Period",sep="--")
        print(" 9:10-10:00"," 10:00-11:00"," 11:00-12:00"," 12:00-1:00"," 1:00-2:00"," 2:00-3:00"," 3:00-4:00",sep="   ")
        print("\n================================================================================================")
        #nested if statements are used to display the scheduled classes in oriented manner
        if(section==1):
            for i in range(6):
                for j in range(6):
                    print(" ",self.table_sec1[i][j],end="\t\t")
                    if(j==2):
                        print("\t",end=" ")
                print()
        elif(section==2):
            for i in range(6):
                for j in range(6):
                    print(" ",self.table_sec2[i][j],end="\t\t")
                    if(j==2):
                        print("\t",end=" ")
                print()
        elif(section==3):
            for i in range(6):
                for j in range(6):
                    print(" ",self.table_sec2[i][j],end="\t\t")
                    if(j==2):
                        print("\t",end=" ")
                print()
        else:
            for i in range(6):
                for j in range(6):
                    print(" ",self.table_sec2[i][j],end="\t\t")
                    if(j==2):
                        print("\t",end=" ")
                print()
        print("================================================================================================")
        print("Note : Labs sessions are conducted from Monday to Thursday after luch and cannot be changed.")

class login_actions:
    #Admin performable actions
    def admin_login(self):
        while(True):
            #exception handling for invalid choice
            try:
                print("\n================================================================================================")
                print("1.Display Time Tables\n2.Expel Student\n3.Display notice board\n0.Exit")
                action_choice=int(input("Enter your choice :"))
            except:
                print("\nNote : Please enter the respective number of your choice...")
                continue
            if(action_choice>3 and action_choice<0):
                print("\n!!!----Invalid Section---!!!")
            elif(action_choice==1):
                #Displaying all section time tables to admin
                tables_object=tables()
                print("\n\nSection A:")
                tables_object.print_tb(1)
                print("\n\nSection B:")
                tables_object.print_tb(2)
                print("\n\nSection C:")
                tables_object.print_tb(3)
                print("\n\nSection D:")
                tables_object.print_tb(4)
            elif(action_choice==2):
                #to expel a student and delete the details from the database
                database_object=database()
                #checking for the number of student details existing in database 
                if not database_object.student_data_dict:
                    print("\nNo students left to expel...!!")
                else:
                    for i,x in database_object.student_data_dict.items():
                        print("-->",i)
                    #to store the name of student to be deleted from the database
                    expel_student=input("\nEnter the name of the student to be expelled :")
                    if(expel_student in database_object.student_data_dict.keys()):
                        database_object.student_data_dict.pop(expel_student)
                        print("\nStudent details successfully deleted....")
                    else:
                        print("\nStudent with id {0} does not exist...!!".format(expel_student))

            elif(action_choice==3):
                #to display notices posted by students
                #creating database object to access the notice board
                database_object=database()
                #to store the length of the notice list
                cnt=len(database_object.Notice_list)
                if(cnt==0):
                    print("\nNo notices posted to display...!!")
                else:
                    print("\n================================================================================================")
                    for i in range(cnt):
                        print("{}. {}".format((i+1),database_object.Notice_list[i]))
                    print("\n================================================================================================")
                    #to perfrom further actions on notices
                    while(True):
                        try:
                            print("\n1.Clear notice\n0.Exit")
                            choice=int(input("Enter your choice : "))
                        except:
                            print("\nNote : Please enter the respective number of your choice...")
                            continue
                        if(choice==1):
                            database_object.Notice_list.clear()
                            print("\nAll notices archived...!!\n")
                            break
                        elif(choice>1 and choice<0):
                            print("\n!!!----Invalid Section---!!!")
                
                    
            elif(action_choice==0):
                break

            
    #to perfrom student login actions
    def student_login(self):
        while(True):
            #error handling for invalid option request
            try:
                print("\n================================================================================================")
                print("\n1.Change Password\n2.Post Notice\n0.Exit")
                selected_choice=int(input("Enter your choice : "))
            except:
                print("\nNote : Please enter the respective number of your choice...")
                continue
            if(selected_choice>2 and action_choice<0):
                print("\n!!!----Invalid Section---!!!")
            elif(selected_choice==0):
                break
            elif(selected_choice==1):
                entered_username=input("\nEnter your username/id : ").lower()
                database_object=database()
                #verifying student login details
                if(entered_username in database_object.student_data_dict.keys()):
                    entered_password=input("Enter your old password : ")
                    #verifying password to update changes into database
                    if(entered_password==database_object.student_data_dict[entered_username]):
                        newly_entered_password=input("Eneter new password : ")
                        database_object.student_data_dict[entered_username]=newly_entered_password
                        print("\nPassword Successfullly updated...!!")
                        break
                    else:
                        print("\nEntered wrong password\nProcess terminated")
                else:
                    print("\nUsername does not exist ...Invalid Username....!!!")
            elif(selected_choice==2):
                while(True):
                    #error handling
                    try:
                        print("\n================================================================================================")
                        written_notice=input("\nEnter the notice to be posted : ")
                    except:
                        print("\nEnter a valid notice to be posted :")
                    #creating database object to post the notice into the database
                    database_object=database()
                    database.Notice_list.append(written_notice)
                    print("\nNotice successfully posted...")
                    break

            

#class to store admin and student database
class database:
    #to store all the notices/remarks posted by students
    Notice_list=[]
    #to store student details and password
    student_data_dict={}
    #to store admin details [!!--Cannot be changed]
    admin_data_dict={"admin":"0000"}
    #method to insert new student details
    def insert_into_database(self):
        student_name=input("\nEnter your name/login id :").lower()
        #checking if exists in db or not
        if(student_name in self.student_data_dict.keys()):
            print("\nUsername already exists...!!!")
        else:
            #inserting into student_data_dict
            student_pass=input("\nEnter your password[Case sensitive]:")
            self.student_data_dict[student_name]=student_pass
            print("\nSuccessfuly Registered")

    #to login student into database so that they can perform any changes to the database
    def login_student_database(self):
        login_id=input("\nEnter your name/login id :").lower()
        #verifying login details
        if(login_id in self.student_data_dict.keys()):
            account_pass=input("\nEnter your password[Case sensitive] : ")
            if (self.student_data_dict[login_id]==account_pass):
                print("\nSuccessfully logged in...:)")
                login_object=login_actions()
                login_object.student_login()
            else:
                print("\nEntered incorrect password...!!")
        else:
            print("\nEntered name/login id does not exists...!!")

    def admin_login_database(self):
        login_id=input("\nEnter admin id :").lower()
        #verifying login details
        if(login_id == "admin"):
            account_pass=input("\nEnter password[Case sensitive] : ")
            if (account_pass=="0000"):
                #login_object to perform admin login actions
                login_object=login_actions()
                login_object.admin_login()
            else:
                print("\nEntered incorrect password...!!")
        else:
            print("\nIncorrect admin Id...!!")

    def display_notice_list(self):
        pass


#class to select the repective action of the user
class action_performance:
    #to obtain the requested action
    def perform_action(self,action):
        if(action==1):
            while(True):
                #exception handling for invalid choice
                try:
                    print("\n================================================================================================")
                    print("\n1.A\n2.B\n3.C\n4.D\n0.Exit")
                    section_choice=int(input("\nEnter you Section : "))
                except:
                    print("\nNote: Please enter the respective number of your choice")
                    continue
                if(section_choice==0):
                    break
                elif(section_choice>4 and section_choice<0):
                    print("\n!!!----Invalid Section---!!!")
                else:
                    #checked for valid request and the action is performed
                    #after a valid request is passed the print table method is called
                    #tables class object is created when used requests to print table
                    table_access_variable=tables()
                    table_access_variable.print_tb(section_choice)
            print("\nReturn to your respective class")
        elif(action==2):
            #creating database object to access student_database
            database_object=database()
            database_object.insert_into_database()
        elif(action==3):
            #creating database object to access student_database
            database_object=database()
            database_object.login_student_database()
        elif(action==4):
            #creating database object to access admin_login
            database_object=database()
            database_object.admin_login_database()

#main fuction to start the program
def main():
    while(True):
        #exception handling for invalid choice
        try:
            print("\n================================================================================================")
            print("\n1.Display time table\n2.Student Register\n3.Student Login\n4.Admin login\n0.Exit")
            action_choice=int(input("\nEnter you choice : "))
        except:
            print("\nNote: Please enter the respective number of your choice")
            continue
        if(action_choice==0):
            break
        elif(action_choice>4 and action_choice<0):
            print("\n!!!----Invalid Section---!!!")
        else:
            #checked for valid request and the action is performed
            #tables class object is created when used requests to print table
            action_variable=action_performance()
            action_variable.perform_action(action_choice)
    print("\nThank you for using our services...")
            


#calling main function
if __name__=="__main__":
    main()
