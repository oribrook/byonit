
** Django Blog Management Project **

This Django project provides a simple yet powerful blog management system using Django and SQLite as the database backend. 
The project includes URL endpoints for user signup and performing CRUD (Create, Read, Update, Delete) operations on blog posts. 
Additionally, it offers options to filter and sort posts based on author and dates.

** Getting Started ** 
To run the project, follow these steps:

Install the required dependencies by running:
pip install -r requirements.txt

Start the Django development server:
python manage.py runserver

Access the project through one of the following endpoints:

Django Templates:

    http://127.0.0.1:8000/posts
    http://127.0.0.1:8000/post/1

APIs:

    http://127.0.0.1:8000/api/v1/posts
    http://127.0.0.1:8000/api/v1/posts?author=moshe
    http://127.0.0.1:8000/api/v1/posts?created_at=2023-11-26
    http://127.0.0.1:8000/api/v1/posts?sort_by=creation
    http://127.0.0.1:8000/api/v1/posts?sort_by=modification


To perform create/edit/delete operations on posts, sign up with the following credentials or use the superuser account:
Username: ori
Password: 123


Testing
You can find a testing script in the file blog_project/test.py that demonstrates the usage of the provided endpoints.

Contributors
Ori Brook