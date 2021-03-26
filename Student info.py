import csv

def write_csv(info_list):
    
      
    with open('stud_info.csv',mode='a') as csv_file:
        
        
        
              
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            
            writer.writerow(["Name","Age","Phone Number","E-mail address"])
        
        writer.writerow(info_list)


condition=True
stu_num=1
    
while(condition):
    student_info=input("Enter student {} information for in the following format (Name Age Phone_Number E-mail_ID): ".format(stu_num))
        
    student_info_list=student_info.split(" ")
    print("\nEntered information is \nName :{}\nAge :{}\nPhone Number :{}\nE-mail Address:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    check=input("Is the entered information correct(yes/no): ")
      
    if check=="yes":
        write_csv(student_info_list)
        condition_check=input("Do you want to enter information for another student(yes/no): ")
        if condition_check=="yes":
            condition=True
            stu_num=stu_num + 1
        elif condition_check =="no":
            condition=False
        
    elif check =="no":
        
        print("\nPlease re enter the details correctly")