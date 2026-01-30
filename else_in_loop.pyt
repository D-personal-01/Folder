for i in range (10):
    print(i)
    if i==5:
        break

#here else will only run when loop is not terminated by break
#terminates the loop when i==5 abnormally
else:
    print("Loop completed without break")

print("-----")

for i in range (0,10,2):
    print(i)
    if i==5:
        break

#here else will only run when loop is not terminated by break
#loop executes successfully without break
else:
    print("Loop completed without break")