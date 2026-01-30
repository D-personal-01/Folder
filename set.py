set1 = set(map(int, input("Enter set 1 elements separated by space: ").split()))
set2 = set(map(int, input("Enter set 2 elements separated by space: ").split()))

def union(s1,s2):
    try:
        s1.update(s2)
        return s1
    except:
        print("Error in union operation")
    finally:
        print("Operation completed.")

def insec(s1,s2):
    try:
        s1.intersection_update(s2)
        return s1
    except:
        print("Error in intersection operation")
    finally:
        print("Operation completed.")
    
def diff(s1,s2):
    try:
        s1.difference_update(s2)
        return s1
    except:
        print("Error in difference operation")
    finally:
        print("Operation completed.")
    
def sdiff(s1,s2):
    try:
        s1.symmetric_difference_update(s2)
        return s1
    except:
        print("Error in symmetric difference operation")
    finally:
        print("Operation completed.")


ch=0

while(ch != 5):
    
    
    print()
    print("Choose the opration you want to perform   \n 1. Union \n 2. Intersection \n 3. Diffrence \n 4. Symmetric Diffrence \n 5. Exit \n ")
    ch=int(input("Enter the opration number you want to do: "))
    print()


    if(ch==5):
        break
    
    print("Enter how you want to do the opration\n 1. Set1 __ Set2 \n 2. Set2 __ Set1")
    p=int(input())
    if p not in [1, 2]:
        print("Invalid choice")
        continue
    
    if(ch==1):
                if(p==1):
                    set1=union(set1,set2)
                elif(p==2):
                    set2=union(set2,set1)

                    
    elif(ch==2):
                if(p==1):
                    set1=insec(set1,set2)
                elif(p==2):
                    set2=insec(set2,set1)

                    
    elif(ch==3):
                if(p==1):
                    set1=diff(set1,set2)
                elif(p==2):
                    set2=diff(set2,set1)

                    
    elif(ch==4):
                if(p==1):
                    set1=sdiff(set1,set2)
                elif(p==2):
                    set2=sdiff(set2,set1)
    print(set1)
    print("Result:\n Set1=",set1,"\n Set2=",set2)
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")





