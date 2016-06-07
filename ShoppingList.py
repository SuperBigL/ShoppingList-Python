shoppingList = []


#This item shows how to navigate the app
def show_help():

        print("Welcome the shopping app.")

        print("""
SHOW - Show All Items currently on the list
DONE - Finish the list and exit out of the app.
HELP - Show this line.
""")

#This method adds items to a list
def add_item(item):
    shoppingList.append(item)
    print("{} added! You now have {} items.".format(item, len(shoppingList)))

def finish(item):
    print("Here are your items:")
    for item in shoppingList:
        print(item)

    print("In total, you added {} items".format(len(shoppingList)))


def show_item(item):
    for item in shoppingList:
        print(item)

def main():
    show_help()
    while True:
    # Ask for new items
        item = input("Enter your item\n")
        if item == "SHOW":
                show_item(item)
                continue

        elif item == "DONE":
            break

        elif item == "HELP":
            show_help()
            continue

        else:
            add_item(item)



        # List item

main()