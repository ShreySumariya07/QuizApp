# QuizApp in Django

## Introduction
A quiz application created in django to conduct mcq quizzes. The application has the following features :
1) Two types of users can login i.e. Student and Teacher
### For teacher :
  1) Add quizzes from interface
  2) Add questions from interface
  3) View results of students who attempted quiz instantly

### For student :
  1) View available quizzes
  2) Attemp any number of quizzes
  3) Can attempt a quiz multiple number of times
  3) View result of quiz
  4) Shows result of all attempts for a particular quiz
  

## Installation
1) Install python3
2) Install pip for python3
3) Install virtualenv pip install virtualenv or pip3 install virtualenv
4) Create virtual environment and cd into it virtualenv django-quiz --python python3 && cd django-quiz
5) Clone git repository into src folder and cd into it git clone <url> src && cd src
6) Install requirements pip install -r requirements.txt or pip3 install -r requirements.txt
7) Make appropriate database changes to settings module and make migrations using python manage.py makemigrations and then python manage.py migrate
8) Run using python manage.py runserver
