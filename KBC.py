#KBC like questions
c=0
qa=[
    [1,"Which bird is the fastest bird in the world?","c","a. Humming Bird            b.  Black Widow\nc.Falcon            d.Seagul"],
    [2,"From which direction does the sun rises from?","d","a. North         b. South\nc. West           d. East"],
    [3,"Which chemical has the chemical symbol 'Os'?","a","a. Osmium         b. Oxygen\nc.Oganesson            d. Gallium"]
    ]
for i in qa:
    print(i[1])
    print(i[3])
    ans=str(input("Type your option: "))
    if (ans==i[2]):
        print("Correct")
        c=c+1
    else:
        print("Wrong")
if(c==1):
    print("25 Lakh")
elif(c==2):
    print("50 Lakh")
elif(c==3):
    print("1 Crore")
