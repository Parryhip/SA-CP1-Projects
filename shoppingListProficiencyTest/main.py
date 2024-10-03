#Samuel Andelin, Shopping list manager
import time
shoppinglist = []
def add(list):
    itemtoadd = input("What is the name of the item that you want to add to the shopping list?")
    print("Item successfully added.")
    time.sleep(1)
    list.append(itemtoadd)
def remove(list):
    listtostr = ", ".join(shoppinglist)
    print("Here is your list: "+ listtostr)
    time.sleep(1)
    itemtoremove = input("What is the name of the item that you want to remove from the shopping list? \n(Type it the exact same way as you added it)")
    if itemtoremove in list:
        list.remove(itemtoremove)
        print("Item successfully removed.")
        time.sleep(1)
    else:
        print("That is not an item in your list.")
while True:
    action = input("What would you like to do? \nEnter 1 to add item \nEnter 2 to remove item \nEnter 3 to view your list \nEnter 4 to leave the list:\n")
    if action =="1":
        add(shoppinglist)
    elif action =="2":
        remove(shoppinglist)
    elif action =="3":
        listtostr = ", ".join(shoppinglist)
        print("Here is your list so far: "+listtostr)
        time.sleep(2)
    else:   
        print("Have a nice day!")
        break