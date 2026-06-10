print("===================================")
print("      DAILY STUDY TRACKER")
print("===================================")

study_records = []

while True:

    print("\n1. Add Study Record")
    print("2. View Study Records")
    print("3. Show Total Study Hours")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        subject = input("Enter subject name: ")
        hours = float(input("Enter study hours: "))

        record = {
            "subject": subject,
            "hours": hours
        }

        study_records.append(record)

        file = open("study_records.txt", "a")

        file.write(subject + " - " + str(hours) + " hours\n")

        file.close()

        print("Study record added successfully.")

    elif choice == "2":

        if len(study_records) == 0:
            print("No study records found.")

        else:

            print("\n===== STUDY RECORDS =====")

            for record in study_records:

                print("Subject:", record["subject"])
                print("Hours:", record["hours"])
                print("-------------------------")

    elif choice == "3":

        total_hours = 0

        for record in study_records:
            total_hours += record["hours"]

        print("\nTotal Study Hours:", total_hours)

    elif choice == "4":

        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
