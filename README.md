📚 Student To-Do & Notes Web Application

A sleek, modern, and animated web application built with Django to help students manage their academic tasks and organize their notes. Perfect for developers learning Django and web development fundamentals.

https://img.shields.io/badge/Django-4.2.5-green https://img.shields.io/badge/Bootstrap-5.3.0-purple https://img.shields.io/badge/Python-3.8+-blue
📋 Table of Contents

    🚀 Introduction

    ✨ Core Features

    🛠 Technologies Used

    ✅ Prerequisites

    ⚙️ Installation & Setup

    📁 Project Structure

    🧠 How It Works: Django MVT

    🔮 Future Enhancements

    📜 License

🚀 Introduction

Welcome to the Student To-Do & Notes Application! This full-stack web application demonstrates the power of Django framework with a clean, intuitive interface featuring smooth animations and professional design.

Perfect for learning:

    🏗️ Backend development with Django (Models, Views, URLs, Forms)

    🎨 Frontend development with HTML, CSS, and JavaScript

    🔐 User authentication and authorization

    🗄️ Database interaction with Django's ORM

    📱 Responsive web design with Bootstrap

✨ Core Features
🔐 User Authentication

    Secure user registration with email verification

    Login and logout functionality

    User-specific data isolation

✅ Task Management

    Create tasks with title, description, and due date

    View, edit, and delete tasks

    Mark tasks as completed

    Search functionality

📝 Notes Management

    Create detailed notes with title and content

    Full CRUD operations (Create, Read, Update, Delete)

    Search through notes

📊 Dashboard

    Clean overview of recent tasks and notes

    Quick-action buttons for easy creation

    User-friendly statistics

🎨 Modern UI/UX

    Fully responsive design for all devices

    Smooth animations and hover effects

    Animated logo and interactive elements

🛠 Technologies Used

Backend:

    Django 4.2.5

Frontend:

    HTML5, CSS3, JavaScript (ES6+)

    Bootstrap 5.3.0

    Bootstrap Icons

Database:

    SQLite (development)

Tools:

    Git for version control

✅ Prerequisites

Before you begin, ensure you have the following installed:

    Python 3.8 or higher - Download from python.org

    pip - Usually comes with Python

    Git - Download from git-scm.com

Verify installations:
bash

python --version
pip --version
git --version

⚙️ Installation & Setup
Step 1: Clone the Repository
bash

git clone https://github.com/your-username/student_todo_project.git
cd student_todo_project

Step 2: Create and Activate Virtual Environment

macOS/Linux:
bash

python3 -m venv venv
source venv/bin/activate

Windows:
bash

python -m venv venv
.\venv\Scripts\activate

Your command prompt will show (venv) when active.
Step 3: Install Dependencies
bash

pip install -r requirements.txt

Step 4: Set Up Database
bash

# Create migration files
python manage.py makemigrations

# Apply migrations and create database
python manage.py migrate

Step 5: Create Superuser (Optional)
bash

python manage.py createsuperuser

Follow prompts to create admin credentials.
Step 6: Run Development Server
bash

python manage.py runserver

🌐 Access your application: http://127.0.0.1:8000/
🔧 Admin panel: http://127.0.0.1:8000/admin/
📁 Project Structure
text

student_todo_project/
│
├── manage.py                 # Django command-line utility
├── requirements.txt          # Project dependencies
│
├── student_todo_project/     # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI entry point
│
└── todo_app/                 # Main application
    ├── __init__.py
    ├── admin.py              # Django admin configuration
    ├── apps.py               # App configuration
    ├── models.py             # Database models (Task, Note)
    ├── views.py              # Application logic
    ├── urls.py               # App-specific URLs
    ├── forms.py              # Django forms
    ├── tests.py              # Test cases
    │
    ├── templates/            # HTML templates
    │   ├── base.html         # Base template
    │   ├── dashboard.html
    │   ├── registration/     # Auth templates
    │   ├── tasks/            # Task-related templates
    │   └── notes/            # Note-related templates
    │
    └── static/               # Static files
        ├── css/
        │   └── style.css     # Custom styles
        ├── js/
        │   └── main.js       # Custom JavaScript
        └── images/
            └── logo.svg      # Animated logo

🧠 How It Works: Django MVT

Django follows the Model-View-Template (MVT) architecture:
🗄️ Model (models.py)

Defines your data structure and database interactions:
python

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

🧠 View (views.py)

Contains business logic and request handling:
python

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})

🎨 Template (templates/)

HTML files with Django template language:
html

{% for task in tasks %}
<div class="task-card">
    <h3>{{ task.title }}</h3>
    <p>{{ task.description }}</p>
</div>
{% endfor %}

🗺️ URL Dispatcher (urls.py)

Routes URLs to appropriate views:
python

path('tasks/', views.task_list, name='task_list')

🔮 Future Enhancements

Here are some ideas to extend this project:

    🎯 Task Categories/Labels - Organize tasks by type (Homework, Exam, Personal)

    🔔 Due Date Notifications - Email reminders for upcoming deadlines

    📝 Rich Text Editor - Integrate TinyMCE or CKEditor for formatted notes

    👤 User Profiles - Profile pictures and user information

    🌙 Dark Mode - Toggle between light and dark themes

    🖱️ Drag-and-Drop - Reorder tasks with drag-and-drop functionality

    📊 Data Export - Export tasks and notes to PDF/CSV

    🔍 Advanced Search - Filter by date, status, or categories