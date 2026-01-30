set1 = set(map(int, input("Enter elements of Set1: ").split()))
set2 = set(map(int, input("Enter elements of Set2: ").split()))

ch = 0

while ch != 12:
    print("""Set Methods:
            1. isdisjoint                         2. issuperset
            3. issubset                           4. add
            5. remove                             6. discard
            7. delete set                         8. clear set
            9. in keyword                         10. pop
            11. display sets                      12. exit
            """)
    ch = int(input("Enter choice: "))

    if ch == 1:
        print(set1.isdisjoint(set2))

    elif ch == 2:
        print(set1.issuperset(set2))

    elif ch == 3:
        print(set1.issubset(set2))

    elif ch == 4:
        x = int(input("\nEnter element to add in Set1: "))
        set1.add(x)

    elif ch == 5:
        x = int(input("\nEnter element to remove from Set1: "))
        set1.remove(x)

    elif ch == 6:
        x = int(input("\nEnter element to discard from Set1: "))
        set1.discard(x)

    elif ch == 7:
        del set1
        print("\nSet1 deleted")
        break

    elif ch == 8:
        set1.clear()

    elif ch == 9:
        x = int(input("\nEnter element to check in Set1: "))
        print(x in set1)

    elif ch == 10:
        print(set1.pop())

    elif ch == 11:
        print("Set1 =", set1)
        print("Set2 =", set2)
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
