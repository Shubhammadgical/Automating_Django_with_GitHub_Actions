# Automating Django Tests with Github Actions

This article would guide us how to Automating Django Tests with Github Actions.

I took inspiration from this [article](https://www.honeybadger.io/blog/django-test-github-actions/) and the code is explained in this [video](https://shorthillstech-my.sharepoint.com/:v:/p/kapil_jain/EXQ2g7yAzUVPhyee-Fbtvg4Bs-rKTJyM2c7BX9gnFn4Clw?e=AU35BN)

- Prerequisites
  - Create Virtual Environment [video](https://www.youtube.com/watch?v=DhLu8sI9uY4)
  
# Steps to Building a Base Project

1. After creating the virtual environment, install Django with the following code:

```
(env)$ pip install django
```

2. Run below command to start a new Django project:

```
(env)$ django-admin startproject contact_app .
```

3. Run below command to create the app:

```
(env)$ python3 manage.py startapp app
```

4. Next, you have to add the app you just created to the settings.py file.

![Screenshot_20221214_093733](https://user-images.githubusercontent.com/101810595/207503498-f7092e01-ec7c-43c7-b2fc-f21f27c3b071.png)

5. Add below code in the app/modules.py for Set Up the Model. 

```
from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
          return self.full_name
```

6. Add below code in the app/views.py for Set Up the View.

```
from django.shortcuts import render
from .models import Contact

def contact_list_view(request):
    contact = Contact.objects.all()
    return render(request, "app/contact_list.html", {'contact':contact})
```

7. Create a template folder in the app directory to hold the template used to display the blog content. Create a templates/app/contact_list.html file, and paste the following code:

```
<h2>Contact List</h2>
{% for contacts in contact %}
<li>{{ contacts.full_name }}: &nbsp;{{ contacts.phone_number }}</li> <br>
{% endfor %}
```

8. Run below command to migrate the modules:

```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py shell
```

9. Run the following code to add each dataset.

```
>>> from app.models import Contact 
>>> Contact.objects.create(full_name="Shubham Chaurasia",phone_number="3567877909").save()
>>> Contact.objects.create(full_name="SKC",phone_number="684977545778").save()
>>> exit()
```

10. Run Django server by below command and then open your development server on your browser. You will see the list of contacts you just saved in the database.

```
(env)$ python manage.py runserver
```

![Screenshot_20221214_095628](https://user-images.githubusercontent.com/101810595/207505691-92728869-f2c4-4011-8a4c-bba6a08163d5.png)

# Steps How to Write a Unit Test for Django Applications

1. Run below command:

```
(env)$ pip install pytest pytest-django mixer
```

2. Create a file with the name pytest.ini at the root contact_app of your project and paste the below code:

```
[pytest]
DJANGO_SETTINGS_MODULE = contact_app.settings
```

3. Open app folder, you'll see a file with the name tests.py; rename it to test_file.py. Copy and past the below code:

```
import pytest    
from app.models import Contact    

@pytest.mark.django_db #give test access to database  
def test_contact_create():    
    # Create dummy data       
    contact = Contact.objects.create(full_name="Shubham Chaurasia", phone_number="75859538350",)    
    # Assert the dummy data saved as expected       
    assert contact.full_name=="Shubham Chaurasia"      
    assert contact.phone_number=="75859538350"
```

4. Run below command:

```
(env)$ pytest
```

![Screenshot_20221214_100802](https://user-images.githubusercontent.com/101810595/207507369-ebbc03eb-8f58-4965-822b-fc7c59ee62f2.png)

5. Copy and past the below code in the test_file.py file for testing the view:

```
from app.views import contact_list_view 
from django.urls import reverse, resolve
from django.test import RequestFactory

...

@pytest.mark.django_db # 
def test_view():
    path = reverse("contact_list")
    request = RequestFactory().get(path) # get the path for the list of contacts
    response = contact_list_view(request)
    assert response.status_code == 200 # assert status code from requesting the view is 200(OK success status response code)
```

6. Run below command:

```
(env)$ pytest
```

![Screenshot_20221214_100834](https://user-images.githubusercontent.com/101810595/207507372-533eacee-e650-4a23-8be8-7fb0592d3d88.png)

7. Copy and past the below code in the test_file.py file for testing the URL:

```
def test_url():            
    path = reverse('contact_list')
    print(path)     
    assert resolve(path).view_name == "contact_list"
```

8. Run below command:

```
(env)$ pytest
```

![Screenshot_20221214_100846](https://user-images.githubusercontent.com/101810595/207507374-b6ac5fde-ce01-45c7-b2f6-6431ec097305.png)

# GitHub Actions

Run below commands:

```
git init
git add .
git commit -m "message"
git remote add <git_repo_url>
git push -u origin main
```

# Set Up GitHub Actions

1. Navigate to the root of your project and create a file with the path .github/workflows/main.yml and past the below code.

```
name: test_Django
on: [pull_request, push] # activates the workflow when there is a push or pull request in the repo
jobs:
  test_project:
    runs-on: ubuntu-latest # operating system your code will run on
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install flake8
      - run: pip install -r requirements.txt # install all our dependencies for the project
      - run: pytest . # run pytest test
      - run: flake8 . # run flake8 test
```

2. Run below command in root of your project, it will create a requirements.txt file.

```
pip freeze > requirements.txt
```

3. Again push the code to GitHub, go to your project on GitHub and click on the “Actions” tab. You’ll see that your GitHub Actions ran completely and that your application has been tested.

![Screenshot_20221214_102834](https://user-images.githubusercontent.com/101810595/207509772-f8b80ef5-f2be-455e-bab3-f6699cc12982.png)



