import sys
import csv
import pyfiglet#type:ignore
import datetime
from project_msg import cowsay_msg_cow,figlet_msg,cowsay_msg_ghost,cowsay_msg_tux
from validate_email_address import validate_email #type:ignore
def main():
    teacher()


def teacher():
    dec=input("do you have any account (yes/no)  ").lower()
    if "no" in dec:
        create_ac()
        return True
    elif "yes" in dec:
        match_ac()
        return True
    else:
        sys.exit("Invalid answer please check and restart the system")
        return False
    ...

     
def create_ac(): #no
    print(figlet_msg("create account"))
    name=input("Name: ")
    
    email_pass=verfication_of_data()
    email=email_pass[0] # type: ignore
    password=email_pass[1] # type: ignore

    if check_csv_existing(email):
        print(cowsay_msg_tux("you already have an account please login\nyour email exist in our data"))
        match_ac()
        return
        ...

    teacher_data=collect_saved_data()
    '''
    till now i have collected the save data now i need to input created data to my 
    csv file next work to write new data or one another word updating csv file after
    teacher register
    '''
    
    teacher_data["name"].append(name)
    teacher_data["email"].append(email)
    teacher_data["password"].append(password)
    
#writing on csv
    with open("teacher_data.csv",'w',newline='') as file:
        header=['name','email','password']

        sheet=csv.DictWriter(file,fieldnames=header)
        

        sheet.writeheader()
        
        for i in range(len(teacher_data['name'])):
            sheet_row={
                "name":teacher_data['name'][i],
                "email":teacher_data['email'][i],
                "password":teacher_data["password"][i]
                
            }
         

            sheet.writerow(sheet_row)
    
    welcome()
    print(cowsay_msg_tux("welcome your account has been created"))

    ...
def match_ac():
        print(figlet_msg("login"))
        i=0
        while i<3:
        
            email_and_pass=verfication_of_data()
            email=email_and_pass[0]#type:ignore
            password=email_and_pass[1]#type:ignore
            #email="fahm@gmail.com"
            #password="1234"

            with open("teacher_data.csv",'r') as file:
                lines=csv.DictReader(file)
                for line in lines:
                    
                    if email in line['email'] and password in line['password']:
                        welcome()
                        return    
                
                print(cowsay_msg_ghost("user email and password don't match"))    
            i+=1

def verfication_of_data():
    
    while True:
        email=input("email:")
        if validate_email(email):
            is_right_mail=True
            break#email verification    
            ...
        else:
            print(cowsay_msg_ghost("your email is not valid"))
            
    while True:
        password1=input("password: ")
        password2=input("re type your password: ")        

        if password1==password2:
            password=password1
            is_right_pass=True
            break
        else:
            print(cowsay_msg_ghost("password Invlid"))

    if is_right_mail and is_right_pass:
        return email,password



    ...

def collect_saved_data():
    
    names=[]
    emails=[]
    passwords=[]
    with open('teacher_data.csv', mode='r') as file:  
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row['name'])
            emails.append(row['email'])
            passwords.append(row['password'])
    teacher_data={'name':names,'email':emails,'password':passwords}
    return teacher_data
    ...

def check_csv_existing(email):
    email_list=[]
    with open("teacher_data.csv",mode='r') as file:
        read_=csv.DictReader(file)
        
        for line in read_:
            email_list.append(line['email'])
    if email in email_list:
        return True
    else:
        return False
    
    ...

def welcome():
    msg=pyfiglet.figlet_format("wellcome")
    print(msg)
    date=datetime.datetime.now()
    print(f"date:{date.day}-{date.month}-{date.year}\ntime:{date.hour}:{date.minute}")



if __name__=="__main__":
    main()



'''
in this file will make sure that files are accessed by teachers only , so that any one can not
touch the file csv , they need to login fisrt to acces those file
'''
