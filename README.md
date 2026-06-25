# Academic Notes Organizer

A web application for organizing course notes and files.

## Features
- User authentication (register, login, logout)
- Add, view, and delete courses
- Add, view, and delete notes with file upload
- Search in notes

## Installation
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## Technologies
- Django
- SQLite
- HTML/CSS
