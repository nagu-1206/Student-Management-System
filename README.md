🎓 Student Management System

A full-featured Student Management System built using Django, MySQL, Bootstrap, and Chart.js.
This project allows administrators to manage students, track attendance, visualize analytics, and control user access with authentication.

🚀 Features
👨‍🎓 Student Management

Add Student
Edit Student
Delete Student
Search Students
View Student List

📊 Dashboard Analytics
Total Students Count
Students per Department (Bar Chart)
Attendance Percentage Chart
Real-time Data Visualization using Chart.js

📅 Attendance Management

Add Attendance
Edit Attendance
Delete Attendance
Attendance Summary Table
Automatic Attendance Percentage Calculation
Visual status indicators (Present / Absent)

🔐 Authentication System
User Registration (Signup)
Login
Logout

Access restricted using @login_required
Tracks logged-in users

🛢 Database
MySQL Database 

Fully migrated models

Production-ready configuration

🛠 Technologies Used
Technology	Purpose
Python	Backend Programming
Django	Web Framework
MySQL	Database
Bootstrap 5	UI Styling
Chart.js	Data Visualization
HTML5	Frontend Structure

📂 Project Structure
student_project/
│
├── students/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│
├── student_project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── db.sqlite3 (if testing)

⚙️ Installation Guide (Industry-Level MySQL Setup)
🔹 1. Clone Repository
git clone https://github.com/nagu-1206/Student-Management-System.git
cd Student-Management-System

🔹 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

🔹 3. Install Required Packages
pip install django
pip install mysqlclient

🔹 4. Configure MySQL Database
Step 1: Create Database

Login to MySQL:
mysql -u root -p

Create database:
CREATE DATABASE student_db;

Exit:

exit;

Step 2: Update settings.py
Open:
student_project/settings.py


Replace DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

🔹 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

🔹 6. Create Superuser
python manage.py createsuperuser

🔹 7. Run Server
python manage.py runserver


Open in browser:
http://127.0.0.1:8000/

🔐 Authentication Flow
New users can register using Signup
After signup → auto login

All views protected using:
@login_required
Admin panel:
http://127.0.0.1:8000/admin/

📊 Dashboard Analytics
Students Per Department
Bar chart showing number of students in each department.
Attendance Percentage Chart
Displays attendance percentage of each student.
Automatically calculated using:
percentage = (present_days / total_days) * 100

🌐 How to Share with Others (Local Network)
Run server like this:
python manage.py runserver 0.0.0.0:8000
Find your IP:
ipconfig
Share:
http://YOUR_IP:8000

Example:
http://192.168.0.100:8000

👥 How to Track Who Logged In
Option 1: Django Admin
Go to:
Admin → Users

Option 2: Active Sessions
Add in settings.py:
'django.contrib.sessions',
Track sessions in Admin panel.

📈 Future Improvements

Export Student Data to Excel
Role-based Authentication (Admin/Staff)
Email Notifications
Deployment on AWS / Render / Railway
REST API Integration

🎯 Project Highlights
✔ Secure login system
✔ Full CRUD operations
✔ Data visualization
✔ Attendance analytics
✔ Clean Bootstrap UI
✔ Production-ready structure

👩‍💻 Author

Nagashree K N
B.E – Information Science & Engineering

GitHub:
👉 https://github.com/nagu-1206/Student-Management-System

⭐ If You Like This Project
Give it a ⭐ on GitHub to support the project!
