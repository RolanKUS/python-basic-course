while True:
    seconds = int(input("Enter seconds from 0 to 8640000: "))
    if seconds < 0 or seconds > 8640000:
        print("Seconds must be between 0 and 8640000: ")
        continue
    total = seconds

    days = total // (24 * 60 * 60)
    total = total % (24 * 60 * 60)

    hours = total // (60 * 60)
    total = total % (60 * 60)

    minutes = total // 60
    seconds = total % 60

    if days == 1:
        days_world = "day"
    else:
        days_world = "days"
    print(f"{days} {days_world}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    while True:
        choice = int(input(
            "What do we do next?\n"
            " 1. Continne\n"
            " 2. Operator assistance\n"
            " 3. Exit\n"
            "Select an action: "
        ))
        if choice == 1:
            break
        elif choice == 2:
            print(" All operators are busy,please hold.")
            choice_1 = input("Continue or wait for an operator?\n"
                             " 1. Continue\n"
                             " 2. Wait for an operator"
                             "Select an action: "
                             )
            if choice_1 == "1":
                print(" Continuing...")
                break
            elif choice_1 == "2":
                print(" Wait for an operator...")
                exit()
            else:
                print(" Invalid choice, returning to menu")
        elif choice == 3:
            print(" Goodbye!")
            exit()
        else:
            print(" Please select a valid action!")
            continue