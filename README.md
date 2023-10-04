Task Manager Application
This is a Python-based Task Manager application that allows users to manage tasks and generate reports. Users can register new accounts, add tasks, view tasks, generate reports, and display statistics. The application supports two user types: 'admin' with additional privileges and regular users.
To use the application you can use the following login details.
Username: admin
password: adm1n

Features
User Registration:
Users can register by providing a unique username and password.
Usernames are case-insensitive and must be unique.
Add Task:
Users can add tasks by specifying the task's title, description, assigned user, due date, and whether the task is completed.
The task's date of assignment is automatically recorded as the current date.
View All Tasks:
Users can view a list of all tasks, including details such as task title, assigned user, date assigned, due date, and completion status.
View My Tasks:
Users can view a list of tasks assigned to them.
Users can select a task to view detailed information and make updates, such as marking it as completed or editing the due date.
Generate Reports:
Users can generate reports that provide statistics on tasks and users.
Reports include the total number of tasks, completed tasks, uncompleted tasks, overdue tasks, percentage of incomplete tasks, percentage of overdue tasks, and more.
Display Statistics:
Users can view statistics based on the generated reports.
Statistics include information about the total number of tasks and users, percentage of tasks completed, and more.
User Authentication:
Users must log in with valid credentials (username and password).
Users can register and log in as 'admin' with elevated privileges.


Installation
Clone the repository to your local machine:
git clone https://github.com/your_username/Task-Manager-Application.git
Navigate to the project directory:
cd Task-Manager-Application
Run the application:
python task_manager.py


Usage
When prompted, log in with your username and password.
Choose options from the menu to perform various tasks.


Sample Data Files
The application uses two data files: user.txt and tasks.txt. These files store user credentials and task information, respectively.
Sample data is included in these files for reference.


User Types
The application supports two user types: 'admin' and regular users.
'admin' users have additional privileges, such as user registration.


Notes
The application is case-insensitive when validating usernames.
Passwords are case-sensitive.
Contributors
Calvin Dunn


