
#=====importing libraries===========
from datetime import datetime
from datetime import date


#=====Function Section===========
#for the function section I have included all comments within the function for neatness
def open_user_file():
    #here I have defined a fucntion that opens the user file and stores it in a list to later be used
    #I made this a function so that I can call it later on instead of having to rewrite the lines of code
    user_data = []
    with open(r'user.txt', 'r') as f:
        user_file = f.readlines()
    for line in user_file:
        content = line.replace(' ' , '') #here I am cleaning the data and seperating it into index for the list
        content = content.replace('\n' , '')
        content = content.split(',')
        user_data.append(content) #here I append the data into the list created above
    return user_data

def open_task_file():
    file_data = []
    file_dict = {}
    with open(r'tasks.txt' , 'r') as f:
            task_file = f.readlines()
            for count, item in enumerate(task_file,1): #I use the enumerate function to count how many lines and add that count as the index for the dictionary
                data = item.replace('\n', '').lower()
                data = data.strip() #these lines clean the data to a readable format for the list and dictionary
                data = data.split(',')
                file_data.append(data)
                file_dict[count] = data
            return file_data
                
def reg_user():
    user_data = []
    with open(r'user.txt', 'r') as f:
        user_file = f.readlines()
    for line in user_file:
        content = line.replace(' ' , '')
        content = content.replace('\n' , '')
        content = content.split(',')
        user_data.append(content)
    
    while True:
        exists = False
        new_user = input('New username:' ).lower()
        for item in user_data:   
            if new_user == item[0]:
                print('User name already exists.')
                exists = True
        if not exists:
            break
    new_pass = input('Password for the new user: ').lower()     
     
    while True:
        confirm_pass = input('Please confirm the users password: ').lower()
        if new_pass != confirm_pass:
            print('Passwords are not the same.')
            continue
        elif new_pass == confirm_pass:
            break
    registered_user = new_user + ', ' + new_pass 
        
    with open(r'user.txt' , 'a') as f:
        f.write('\n' + registered_user)

def add_task():
    task_username = input('Who is this taks allocated to: ').lower()
    task_title = input('What is the title of the task: ').lower()
    task_description = input('Description of the task: ').lower()
    task_due_date = input('When is the task due: ').lower()
    today_date = datetime.today().strftime('%d %B %Y')
    task_done = 'no'
    new_task = '\n' +  task_username + ', ' + task_title + ', ' + task_description + ', ' + task_due_date + ', ' + today_date + ', ' + task_done
     
    with open(r'tasks.txt', 'a') as f:
        f.write(new_task)

def view_all():
     with open(r'tasks.txt' , 'r') as f:
            task_file = f.readlines()
            for line in task_file:
                data = line.split('\n')
                data = line.split(',')
                print('_____________________________________________________')
                print('Task:                ' + data[1])
                print('Assigned to:          ' + data[0])
                print('Date Assigned:       ' + data[4])
                print('Due Date:            ' + data[3])
                print('Task Complete:       ' + data[5])
                print('Task Description:' + '\n' + data[2])
                print('_____________________________________________________')

def view_mine():
    file_data = []
    file_dict = {}
    with open(r'tasks.txt' , 'r') as f:
            task_file = f.readlines()
            for count, item in enumerate(task_file,1):
                data = item.split('\n')
                data = item.split(',')
                file_data.append(data)
                file_dict[count] = data        
                if username == data[0]:
                    print('_____________________________________________________')
                    print('Task Number:         ', count) #here we print the count of how many lines were counted above for the task number
                    print('Task:                ' + data[1])
                    print('Assigned to:          ' + data[0])
                    print('Date Assigned:       ' + data[4])
                    print('Due Date:            ' + data[3])
                    print('Task Complete:       ' + data[5])
                    print('Task Description:' + '\n' + data[2])
                    print('_____________________________________________________')  
    #I have asked the user for a chocie and take that choice through to another function later, I also give the option to return to the main menu
    #by inserting -1 as an option  
    choice = input('Please enter a task number or -1 to return to the main menu: ')
    if choice == '-1':
       return menu
    #if the user chooses any other option other than -1 it will take the users choice and the lists, dictionarys into the new function
    else:
        user_choice(choice, file_data, file_dict) #here I call the new function I have defined below
        
def user_choice(choice, file_data, file_dict):
    #I set a variable task equal to the dictionary so that I can pull through all relevant data to display
    task = file_dict[int(choice)]   
    print('_____________________________________________________')
    print('Task Number:         ', choice)
    print('Task:                ' + task[1])
    print('Assigned to:          ' + task[0])
    print('Date Assigned:       ' + task[4])
    print('Due Date:            ' + task[3])
    print('Task Complete:       ' + task[5])
    print('Task Description:' + '\n' + task[2])
    print('_____________________________________________________')
    
    #here I give the user options on what they would like to do.
    #if the user chooses yes it will change the completed to yes and overwrite it into the text file
    #if the user chooses to edit then it will allow them too edit the date
    task_editor = input('''Would you like to mark this task as complete or edit the task?
Enter Yes to mark the task as complete.
Enter edit if you would like to edit the task. 
Enter -1 to return to the menu.
Please enter your choice: ''').lower()
    if task_editor == -1:
        return menu
    elif task_editor == 'yes':
        task[5] = ' yes'
    elif task_editor == 'edit':
        print('You are only allowed to change the due date:')
        new_due_date = input('What is the new due date: ').lower()
        task[3] = ' ' + new_due_date
    
    with open(r'tasks.txt', 'w') as f:
        f.write('')
    #I use a for loop to itterate through the list to convert it into a string to write back into the text file.    
    for line in file_data:
        my_string = line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5]
        with open(r'tasks.txt', 'a') as f:
            f.write(str(my_string))                 

def generate_reports():
    #I call my opening fucntions I defined in the beginning to avoid having to write the lines of code again
    task_reports_file = open_task_file()
    user_reports_file = open_user_file()
    
#total number of tasks generated
#here I set a count variable to add one for every line in the task_reports_file    
    task_count = 0
    for line in task_reports_file:
        if line:
            task_count += 1
    total_number_of_tasks = task_count
    
#total number of completed tasks
#here I set a count to count every yes in the completed tasks to later use
    completed_count = 0
    for line in task_reports_file:
        if line[5] == ' yes':
            completed_count += 1
    
#total number of uncompleted tasks
#here I count the uncompleted tasks to later use for a calculation
    uncompleted_count = 0
    for line in task_reports_file:
        if line[5] == ' no':
            uncompleted_count += 1

#total number of uncompleted tasks and overdue 
#I set a variable today by calling the datetime module
#I then itterate through the reports file and compare the the today date with the due date to see if it overdue
    today = datetime.today()
    over_due_tasks = 0
    for line in task_reports_file:
        due_date =''.join(map(str,line[3])) #here I had to join the line[3] which makes it comparable
        due_date = datetime.strptime(due_date, " %d %b %Y") #here I set the format of the due date so that it can be compared
        if (due_date < today) and line[5] == ' no':
            over_due_tasks += 1
    
#percetange of tasks that are incomplete
    percentage_incom = str(round((uncompleted_count/total_number_of_tasks)*100)) + '%'
        
#percentage of tasks that are overdue
    percentage_overdue = str(round((over_due_tasks/total_number_of_tasks)*100)) + '%'
    with open('task_overview.txt', 'w') as f:
        l1 = 'The total number of tasks generated are: ' + str(total_number_of_tasks) + '\n'
        l2 = 'The total number of completed tasks are: ' + str(completed_count) + '\n'
        l3 = 'The total number of uncompleted tasks are: ' + str(uncompleted_count) + '\n'
        l4 = 'The total number of overdue tasks are: ' + str(over_due_tasks) + '\n'
        l5 = 'The percentage of incomplete tasks is: ' + str(percentage_incom) + '\n'
        l6 = 'The percentage of taks that are overdue is: ' + str(percentage_overdue) + '\n'
        f.writelines([l1 , l2, l3, l4, l5, l6])
        
#total number of users registered
#here I make a count variable to keep track of every line in the file, same as above
    user_count = 0
    for line in user_reports_file:
        if line:
            user_count += 1
    total_number_of_users = user_count
    
#here I set the new text file as write+ so that I can write information into it
#I have kept this seperate from the loop so that it does not duplicate into the text file and only write once 
    f = open('user_overview.txt', 'w+')
    a1 = 'The total number of users registered are: ' + str(total_number_of_users) + '\n'
    a2 = 'The total number of tasks generated are: ' + str(total_number_of_tasks) + '\n'
    a3 = '\n'
    f.writelines([a1, a2, a3])
    
    #here I start a for loop and set several variablesto later use and call
    for line in  user_reports_file:
        today = datetime.today() #setting todays date
        over_due_tasks = 0
        total_tasks_assigned = 0
        completed_count = 0
        uncompleted_count = 0
        username_check = line[0] #this line check that the user names are the same if they are it move onto the next step
        for line in task_reports_file:
            task_user_check = line[0]
            if username_check == task_user_check: #here we check if the username and task user name are the same
                total_tasks_assigned += 1
                if line[5] == ' yes':
                    completed_count += 1
                elif line[5] == ' no':
                    uncompleted_count += 1
                due_date =''.join(map(str,line[3])) #here I change and join the date time to compare the two dates
                due_date = datetime.strptime(due_date, " %d %b %Y")
                if (due_date < today) and line[5] == ' no':
                    over_due_tasks += 1
        if total_tasks_assigned > 0:
            #total number of tasks assigned to a specific user            
            user_overview = ('Total number of tasks assigned to ' + str(username_check) + ' is: ' + str(total_tasks_assigned))
            #percentage of tasks assigned to the user from the total tasks
            percentage_assigned =('The percentage of assigned tasks to ' + str(username_check) + ' is: ' + str(round((total_tasks_assigned/total_number_of_tasks)*100)) + '%')
            #percentage of tasks for the user that have been completed
            percentage_complete =('The percentage of tasks that have been completed for ' + str(username_check) + ' is: ' + str(round((completed_count/total_tasks_assigned)*100)) + '%')
            #percentage of tasks for user that must still be completed
            percentage_incom_for_user =('The percentage of tasks that must still be completed for ' + str(username_check) + ' is: ' + str(round((uncompleted_count/total_tasks_assigned)*100)) + '%')
            #percentage of tasks assigned to user that are overdue
            percentage_overdue_for_user =('The percentage of overdue tasks for ' + str(username_check) + ' is: ' + str(round((over_due_tasks/total_tasks_assigned)*100)) + '%')
            #I have included this in on the loop so that it loops though for every calculation and line in the task file
            f.write('Summary for ' + username_check + '\n')
            f.write(user_overview + '\n')
            f.write(percentage_assigned + '\n')
            f.write(percentage_complete + '\n')
            f.write(percentage_incom_for_user + '\n')
            f.write(percentage_overdue_for_user + '\n')
            f.write('\n')
        
def display_statistics():
    #I generate the reports first so that if the user did not do that first it is done and the data can be used
    generate_reports()
    file_data = []
    file_dict = {}
    #here I open the task_overview file that was created so we cna read data from it
    with open('task_overview.txt', 'r') as f:
        task_file = f.readlines()
        #below I clean up the data and append it to the list and dictionary
        for count, item in enumerate(task_file,1):
                data = item.replace('\n', '')
                file_data.append(data)
                file_dict[count] = data
        #we print the summary and file data for the user
        print('__________________________________________________')
        print('The summary for the amount of tasks is below: ') 
        print('\n')       
        print(file_data[0])
        print(file_data[1])
        print(file_data[2])
        print(file_data[3])
        print(file_data[4])
        print(file_data[5])
        print('__________________________________________________')
        
    file_data = []
    file_dict = {}
    #I open the user_overview file to gather data from it into the variables above
    with open('user_overview.txt', 'r') as f:
        task_file = f.readlines()
        print('\n')
        print('__________________________________________________')
        #below I clean up the data and append it to list and dictionary
        for count, item in enumerate(task_file,1):
            data = item.replace('\n', '')
            file_data.append(data)
            file_dict[count] = data
        #here we print the data out for the user to view in a user friendly way
            print(data)

#=====Function Section===========

#====Login Section====
#this is the log in section and the code has not changed since the prior submission
user_data = []
with open(r'user.txt', 'r') as f:
    user_file = f.readlines()
    for line in user_file:
        content = line.replace(' ' , '')
        content = content.replace('\n' , '')
        content = content.split(',')
        user_data.append(content)

while True:
    correct = False
    print('Please login with your relevant credentials.')
    username = input('Username: ').lower()
    password = input('Password: ').lower()
    for item in user_data:   
        if username == item[0] and password == item[1]:
            print('Credentials correct.')
            correct = True
            break
        elif username == item[0] and password != item[1]:
            print('Your password is incorrect. ')
            correct = False
        elif username != item[0] and password == item[1]:
            print('Your username is incorrect')
            correct = False
        else:
            print('Your credentials are incorrect.')
    if correct:
        break
#====Login Section====

#====Menu Section====
registered_user = 0
while True:
    if username == 'admin':
        menu = input(''' select on of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()
    else: 
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()


    if menu == 'r' and username == 'admin':
        pass
        reg_user()
        
    elif menu == 'a':
        pass
        add_task()           

    elif menu == 'va':
        pass
        view_all()
                
    elif menu == 'vm':
        pass
        view_mine() 
    
    elif menu == 'gr':
        pass
        generate_reports()
    
    elif menu == 'ds':
        pass
        display_statistics()         
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
#====Menu Section====