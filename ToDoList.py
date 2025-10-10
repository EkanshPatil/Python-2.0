tasks = []
# fruits= ["apple","grape","orange","apple"]
# print(fruits)
# for i in fruits:
#     print(i)
while True:
    print("To do list:")
    print("1-View tasks")
    print("2-Add a task")
    print("3-Remove a task")
    print("4-Exit list")
    print("5-Change task")
    print("6-Mark task complete")

    choice = int(input("Pick one of the above numbers(1-6)" ))

    if choice == 1:
        for i in tasks:
            print(i)
    
    elif choice ==2:
        task = input("Add a task ")
        tasks.append(task)
        print("Task added!")

    elif choice ==3:
        task = input("What do you want to remove? (enter the name of the task)")
        tasks.remove(task)     
        print("Task removed!")

    elif choice ==4:
        print("Thanks for using list bot 3.0! exiting game now...")    
        break
     

    elif choice ==5:
        task = input("Enter the task that you want to change (enter the name of the task)")
        number =   tasks.index(task)
        replace = input("Enter the tast that you want to replace it with")
        tasks[number] = replace   
        print("Task replaced!")
    
    elif choice ==6:
        task = input("Enter the name of the task that you want to mark complete (enter the name of a task)")
        number = tasks.index(task)
        tasks[number] = task+" -completed!"
        print("Task marked complete!")
    
    else :
        print("incorrect value entered please enter a number between 1 and 6 either pick  either 1,2,3,4,5 or 6and do not enter the commas")    