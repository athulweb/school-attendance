# School Attandence Managment System
import pickle
import numpy as np

# Datas 

students = None
statics = []

def backup():
    school = {"statics": statics , "students" :students}
    with open("school.pkl","wb") as file:
        pickle.dump(school , file)


def start():
    total = input("How much students are in your class : ")
    boys = input("How many boys :")
    girls = input("How many girls :")
        
    try :
        total =int(total)
        boys =int(boys)
        girls =int(girls)
    except ValueError :
        print("The data you entered is not numbers")

    if boys > total :
            print(f"You said you only have {total} students but your number of boys is more than it. ")
    if girls > total :
        print(f"You said you only have {total} students but your number of girls is more than it. ")
    if boys+girls != total:
        print("The number of boy's and girl's sum is not the total so , somthing went wrong in your side")

    students = np.zeros((total , 30), dtype=int)
    statics = {}

    print("Students have been successfully created you needed to be give them names")
    print("Now you needed to give the students name and roll numbers are already declared by our mechine")
    for rollno in range(total) :
        name = input(f">> Enter name of student belong to the role number ({rollno+1}) : ")
        statics[rollno] = {"name":name, "present":students[rollno]  }
    
    return students , statics 


def attendance():
    input

def main():
    print("School Attandance system")
    print("\n")
    print("Click 1 to take Setup")
    print("Click 1 to Backup the datas")

    while True :
        q =input(">> : ")
        
        if q == "1":
            students , statics = start()
        elif q == "2":
            backup()