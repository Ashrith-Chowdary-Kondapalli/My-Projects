# Turns normal numbers into seperated numbers with commas

while True: 

    try:
            donation = int(input("Enter the amount you would like to donate: "))
            confirmation = input(f"Are you sure you want to donate ${donation}? (yes/no): ")

            if confirmation == "yes":
                print(f"Thank you for your generous donation of ${donation:,}!")

                break

            else:
                print("Donation cancelled.")