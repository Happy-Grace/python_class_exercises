# Classwork with Teacher

def insertList(menuList):
    item = input("Enter an  item to the menu List: ")
    menuList.append(item)

def removeList(menuList):
    item = input("Enter an item to be removed from the List: ")
    menuList.remove(item)

def sortList(menuList):
    print("\nRe-arranges the items in the list in an orderly (ascending) manner.")
    menuList.sort()

def reverseList(menuList):
    print("\nReverse is the opposite of sort() method.\nIt rearranges the list in a descending order.")
    print("NOTE: Reverse cannot work efficiently without first using the Sorting.")
    menuList.reverse()

def showList(menuList):
    for item in menuList:
        print(item)

def extendList(menuList):
    print("\nEnter the items you want to extend to the main list\nMultiple items can be inputted with space (e.g: Mirror Powder etc.)")
    inpItem = input("\nEnter the items you want to extend(e.g: Mirror Powder etc.): ")
    menuList1 = list(inpItem.split())
    menuList.extend(menuList1)

def inserts(menuList):
    print("This is used when you know the index you desire to insert/input your item(s) to the menu List.\n")
    value = int(input("Enter your desired index value: "))
    item = input("Enter the item you desire to insert into the list: ")

    menuList.insert(value, item)

def popList(menuList):
    print("This is used when you know the index you desire to remove/delete items) from the menu List.\n")
    value = int(input("Enter your desired index value: "))

    menuList.pop(value)

def quitList():
    exit()


menuList = []

while ("True"):
    print("1. Insert an item into the List.")
    print("2. Remove an item from the List.")
    print("3. Sort the items in the List.")
    print("4. Reverse the items in the List.")
    print("5. Show/Display the items in the List.")
    print("6. Extend the items of the List.")
    print("7. Inserting items to the list using the insert() method.")
    print("8. Removing items from the list using the pop() method.")
    print("9. Quit the List.")


    try:
        inp = input("\nEnter an option from 1 - 9: ")
        choice = int(inp)

        if choice == 1:
            insertList(menuList)
            print("")

        elif choice == 2:
            removeList(menuList)
            print("")

        elif choice == 3:
            sortList(menuList)
            print("")

        elif choice == 4:
            reverseList(menuList)
            print("")

        elif choice == 5:
            showList(menuList)
            print("")

        elif choice == 6:
            extendList(menuList)
            print("")

        elif choice == 7:
            inserts(menuList)
            print("")

        elif choice == 8:
            popList(menuList)
            print("")

        elif choice == 9:
            break
            # quit()


    except:
        print("\nInvalid Input! Enter an option from 1 - 9!!\n")
        continue