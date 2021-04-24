import csv
def write_into_csv(into_list):
    with open("student_info.csv","a", newline="")as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            
            writer.writerow(["name","age","phone no.","email ID"])
            writer.writerow(into_list)


print("this program prints the student info.\n")


condition =True
while(condition):
    student_info=input("enter the information of student {name age contact_no. email} \n")
    print("entered info is"+ student_info)
    student_info_list = student_info.split(' ')
    print("enterd split info is"+ str(student_info_list))
    
    print("enterd split info is name {} age {} phone {} email {}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    write_into_csv(student_info_list)
    
    condition_check=input("if you want to enter student enter yes else no:\n")
    if condition_check == "yes":
        condition=True
    elif condition_check == "no":
        condition= False
    else :
        print("enter yes or no only")
    

    
