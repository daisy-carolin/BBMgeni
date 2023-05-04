# BBMgeni
Mgeni App (Mgeni App) is a software application designed to track, manage and record the visitors to a facility or premises. It is an important component of modern security systems for businesses, organizations, and government institutions. The Mgeni App automates the visitor registration process and ensures that only authorized visitors are allowed to enter the premises.

The purpose of a Mgeni App is to improve the security and safety of a facility by providing accurate and up-to-date information about the visitors. It also helps to streamline the check-in process, reduce wait times, and enhance the overall visitor experience.

# Built With
 `-Python Django`
 `-HTML/CSS`
 `-SCSS`
 `-Javascript`

# Prerequisites
To get this project up and running locally, you must already have python virtual environment plus the necessary requirements.txt  installed on your computer.You also need 
`python 3.8 version`

# Installation
1.Then install virtualenv:

`sudo pip install virtualenv`

2.Create a virtualenv for {{ project_name }} and activate it:

`virtualenv -p <PYTHON_3_PATH> ~/virtualenvs/{{ project_name }}`

`source ~/virtualenvs/{{ project_name }}/bin/activate`
3.Install Django into the virtualenv:

`pip install Django`

4.Now, install the rest of the packages that are required by your Django project:

`pip install -r requirements.txt`

5.Setup the database. Locally, this will create a new sqllite database

6.Start the Django server:

`python manage.py runserver`
