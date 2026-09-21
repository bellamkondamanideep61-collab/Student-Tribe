reports = []


def add_item(item_type):
    print("\nAdd", item_type, "item")

    id = input("Enter ID: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    location = input("Enter location: ")
    date = input("Enter date (YYYY-MM-DD): ")

    if id == "" or category == "" or description == "" or location == "":
        print("Please enter all details")
        return

    item = {
        "id": id,
        "type": item_type,
        "category": category,
        "description": description,
        "location": location,
        "date": date,
        "status": "Open"
    }

    reports.append(item)

    print("Item added successfully")


def show_items():
    if len(reports) == 0:
        print("No reports available")
        return

    for item in reports:
        print("\n--------------------")
        print("ID:", item["id"])
        print("Type:", item["type"])
        print("Category:", item["category"])
        print("Description:", item["description"])
        print("Location:", item["location"])
        print("Date:", item["date"])
        print("Status:", item["status"])


def search_items():
    category = input("Enter category: ").lower()
    location = input("Enter location: ").lower()

    found = False

    for item in reports:

        if item["category"].lower() == category and \
           item["location"].lower() == location:

            print("\nID:", item["id"])
            print("Type:", item["type"])
            print("Description:", item["description"])
            print("Location:", item["location"])
            print("Status:", item["status"])

            found = True

    if found == False:
        print("No matching items found")


def find_match():
    id = input("Enter lost/found item ID: ")

    selected = None

    for item in reports:
        if item["id"] == id:
            selected = item

    if selected == None:
        print("Item not found")
        return

    found = False

    for item in reports:

        if item["id"] == selected["id"]:
            continue

        if item["type"] == selected["type"]:
            continue

        score = 0

        if item["category"].lower() == selected["category"].lower():
            score = score + 40

        if item["location"].lower() == selected["location"].lower():
            score = score + 30

        words1 = selected["description"].lower().split()
        words2 = item["description"].lower().split()

        common = 0

        for word in words1:
            if word in words2:
                common = common + 1

        score = score + common * 10

        if score > 100:
            score = 100

        if score >= 40:

            print("\nPOSSIBLE MATCH FOUND")
            print("First Item:", selected["id"])
            print("Second Item:", item["id"])

            if item["category"].lower() == selected["category"].lower():
                print("Category Match: Yes")
            else:
                print("Category Match: No")

            if item["location"].lower() == selected["location"].lower():
                print("Location Match: Yes")
            else:
                print("Location Match: No")

            print("Common Keywords:", common)
            print("Match Score:", score)

            if score >= 70:
                print("Confidence: High")
            elif score >= 50:
                print("Confidence: Medium")
            else:
                print("Confidence: Low")

            print("Status: Review Required")

            found = True

    if found == False:
        print("No possible match found")


def change_status():
    id = input("Enter item ID: ")

    for item in reports:

        if item["id"] == id:

            print("1. Open")
            print("2. Matched")
            print("3. Returned")

            choice = input("Enter choice: ")

            if choice == "1":
                item["status"] = "Open"

            elif choice == "2":
                item["status"] = "Matched"

            elif choice == "3":
                item["status"] = "Returned"

            else:
                print("Wrong choice")
                return

            print("Status changed")
            return

    print("Item not found")


def show_open():
    found = False

    for item in reports:

        if item["status"] == "Open":
            print("\nID:", item["id"])
            print("Type:", item["type"])
            print("Category:", item["category"])
            print("Description:", item["description"])
            print("Location:", item["location"])

            found = True

    if found == False:
        print("No open reports")


while True:

    print("\n============================")
    print("     LOST AND FOUND")
    print("============================")

    print("1. Add Lost Item")
    print("2. Add Found Item")
    print("3. Search Items")
    print("4. Find Possible Match")
    print("5. Change Status")
    print("6. Show Open Reports")
    print("7. Show All Reports")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item("Lost")

    elif choice == "2":
        add_item("Found")

    elif choice == "3":
        search_items()

    elif choice == "4":
        find_match()

    elif choice == "5":
        change_status()

    elif choice == "6":
        show_open()

    elif choice == "7":
        show_items()

    elif choice == "8":
        print("Program ended")
        break

    else:
        print("Invalid choice")