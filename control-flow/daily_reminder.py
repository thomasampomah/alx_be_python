task = input("Please enter a task description: ")
priority = input("Is it a high/medium/low task: ")
timing = input("Is it time-bound. (yes/no): ")


match priority:
    case("high"):
        if timing == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today")
        else: 
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time")
    case("medium"):
        if timing == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time")
    case("low"): 
        if timing == "yes" :
            print(f"Reminder: {task} is a low priority task that requires immediate attention today!")
        else:
            print(f" Note: {task} is a low priority task. Consider completing it when you have free time.")

