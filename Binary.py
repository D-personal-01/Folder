import pickle
#Create record
def create():
    f=open("stud.dat","ab")

    roll=int(input("Enter roll number: "))
    CGPA=float(input("Enter CGPA: "))
    pickle.dump([roll,CGPA],f)
    
    f.close()

    
#Display
def display():
    
    f=open("stud.dat","rb")
    
    try:
        while 1:
            s=pickle.load(f)
            print(f"\nRoll:{s[0]}\nCGPA:{s[1]}\n")
    except EOFError:
        pass
    
    f.close()
#Search student record
def search():
    f=open("stud.dat","rb")
    roll=int (input("Enter the roll number of the student: "))
    try:
        while 1:
            s=pickle.load(f)
            if s[0]==roll:
                print(f"\nRoll:{s[0]}\nCGPA:{s[1]}\n")
                f.close()
                return[s[0],s[1]]
    except EOFError:
        print("Student record not found ")
        f.close()

    
#Update CGPA
def update():
    f=open("stud.dat","rb+")

    roll=int (input("Enter the roll number of the student: "))
    
    try:
        while 1:
            pos=f.tell()
            s=pickle.load(f)
            if s[0]==roll:
                print(f"\nRoll: {s[0]}\nCGPA: {s[1]}\n")
                CGPA=float(input("Enter the new CGPA: "))
                f.seek(pos)
                s[1]=CGPA
                pickle.dump(s,f)
                print("Record saved.")
                break
    except EOFError:
        print("Record not found.")
                    
    f.close()

    
#Delete student record
def delete():
    roll = int(input("Enter roll number to delete: "))
    
    data = []

    try:
        with open("stud.dat", "rb") as f:
            while True:
                data.append(pickle.load(f))
    except EOFError:
        pass

    new_data = []
    found = False

    for record in data:
        if record[0] != roll:
            new_data.append(record)
        else:
            found = True

    with open("stud.dat", "wb") as f:
        for record in new_data:
            pickle.dump(record, f)

    if found:
        print("Record deleted successfully!")
    else:
        print("Record not found.")

    

print ("                                                                                   ------WELCOME TO STUDENT FILE------")

c=0

while c!=6:
        print ('''\n\nWhat opration do you want to perform:
                                                                                             1. Create a record.
                                                                                             2. Display record.
                                                                                             3. Search record.
                                                                                             4. Update record.
                                                                                             5. Delete record.
                                                                                              6. Exit.''')

        c=int(input("Enter the searies number to do do the opration: "))

        if c==1:
            create()
        elif c==2:
            display()
        elif c==3:
            search()
        elif c==4:
            update()
        elif c==5:
            delete()
        elif c==6:
            break
        else:
            print ("Incorrect choice please choose again.")















