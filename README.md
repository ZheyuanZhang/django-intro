This is a basic Django project designed as an introduction to Django and to test familiarity with HTML, CSS and Bootstrap  
  
Instructions:  
  
## 1. Clone Repository in to your local environment  
  
## 2. Create and activate a Python3 virtual environment  
python3 -m venv venv  
or use pyenv <https://github.com/pyenv/pyenv-virtualenv>  

## 3. Install requirements  
pip install - r requirements.txt

## 4. Run Server and go to /index
run server using the manage.py file  
``
python manage.py runserver  
``  
!!Ignore Migrations. There is no database for this project !!  
go to /index  
  
## 5. Implement the designs  
New designs for the /index can be found at  
Desktop: <https://github.com/singlekey-screening/django-intro/blob/master/main/static/assets/Form%20submission%20test%20v2.png>  
Mobile: <https://github.com/singlekey-screening/django-intro/blob/master/main/static/assets/Form%20submission%20test%20-%20responsive%20v2.png>  
  
The goal is to create a responsive view that looks like the Desktop design on a large screen and the Mobile design on small screens. This can be achieved by having the results cards change shape depending on the view, or by having two separate HTML chunks that are made visible or invisible depending on the size of the screen (for instance using the boot strap class 'd-xl-none d-block' will make a section visible on all screens but xl screens and 'd-none d-md-flex' will make a section invisible on screens smaller than medium sized)
  
!! Please Note: Bootstrap <https://getbootstrap.com/docs/4.0/getting-started/introduction/> is installed in the base template so you can use Bootstrap Classes in any template that extends base.html. If you are not familiar with Bootstrap, you do not have to use it, but if you are familiar, please use as much Bootstrap as necessary  
  
The SingleKey logo can be found in the main/static/assets folder

## 6. (Optional) Persist the data  
This project is designed with the hope that it wont take up too many hours, however if you have time, find a way WITHOUT A DATABASE to persist new submissions and display them on index.html.  

## Additional Experiment  
Feel free to try any other experimenting, such as:  
-add submission time to the submissions  
-ensure emails are formatted properly  
-adding new routes  
-implementing some api integration  
-using built in Django functionality like django forms  

## Commit your work to a public Git repository  
When you are happy with your work, commit your work to a public git repository.  If you make multiple commits, try to make each commit tell a coherent story about what you were thinking/implementing.  

