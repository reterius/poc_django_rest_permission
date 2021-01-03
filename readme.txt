This rest api is an example for django rbac and permission structure. Roles are 'admin' and 'anonymous'. Its a poc working example.

1) python3 -m venv venv
2) source venv/bin/activate
3) pip install -r requirements.txt
4) python manage.py makemigrations
5) python manage.py migrate
6) python group.py (To add 'admin', 'anonymous' groups)
7) python manage.py createsuperuser (To create user which name of 'admin' user. We must set '1' as its group id to determine as 'admin' type of user)
   - Note your password. Yo will use it to authentication from login api via username(admin)
   - You can check whether it was created user named 'admin' from 'user_user' table on database
8) python manage.py createsuperuser (To create user which name of 'normal_user' user. We must set '2' as its group id to determine as 'anonymous' type of user)
   - Note your password. Yo will use it to authentication from login api via username(normal_user)
   - You can check whether it was created user named 'normal_user' from 'user_user' table on database
9) python manage.py runserver (To run application)
10) Api documentation https://documenter.getpostman.com/view/5458897/TVt2cj4t


TO DO:
1) JWT Integration
2) UNit tests
3) Response Abstractions
4) Dockerize working