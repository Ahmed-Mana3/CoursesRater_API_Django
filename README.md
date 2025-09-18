Course Rater API
Introduction

Course Rater is a Django REST Framework (DRF) based API that allows users to browse courses, rate them, and manage ratings. It also supports channels for grouping courses and provides authentication with token-based access.

Features

User authentication with token-based login.

CRUD operations for Courses, Channels, and Users.

Rate and review courses (1–5 stars with optional comments).

Automatic token creation for new users.

Admin panel support.

Installation

Clone the repository:

git clone https://github.com/Ahmed-Mana3/CoursesRater_API_Django.git
cd course_rater


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the server:

python manage.py runserver

Usage

API root: http://127.0.0.1:8000/

Obtain token: POST http://127.0.0.1:8000/token-request/

Example endpoints:

/courses/ – list or create courses.

/courses/{id}/rate_course/ – rate or update a course.

/rates/ – view all ratings.

/channels/ – manage channels.

/users/ – manage users (admin only).

Dependencies

Django

Django REST Framework

Django REST Framework Authtoken
