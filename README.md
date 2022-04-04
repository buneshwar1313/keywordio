# keywordio
django rest api


# api
Registration api
api: 127.0.0.1:8000/api/register/
request Type : Post 

Login api
api 127.0.0.1:8000/api/Login/
request Type : get 
token created 

Logout api 
api 127.0.0.1:8000/api/Logout/
request Type : get

Get  List of all books and create Books
api : 127.0.0.1:8000/api/book/
request Type : get & post 

Update , Delete , Put for all Books
api: 127.0.01:800/api/book/<int:id>/
request Type : update , put , delete 


Installation process
1. unzip file 
2. create environment
3. install requirements.txt (pip3 install -r requirements.txt)
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. python3 manage.py runserver
7. 
