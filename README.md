# Project Mono

No seas un mono

Don't be a monkey

Work smart!

Mono is Spanish for Monkey

## How to install 
###A project with Python and Django

install Python3
brew install python
brew upgrade python

install PIP

Depends on:

python3 -m pip install django
python3 -m pip install requests
python3 -m pip install simplejson
python3 -m pip install sklearn

##Start the server

./manage.py runserver

Go to

http://localhost:8000/incidentmanagement/

## To create an new user:

python manage.py createsuperuser

## Open admin console

http://localhost:8000/admin/login/?next=/admin/

Do the obvious, something something
admin
admin


## Deploy on PCF

Use the python_buildpack. 

cf push mono -b python_buildpack -c "null"

cf push mysite -p . -c "python ./im/mysite/manage.py runserver" -b python_buildpack -u none

Please read the manifest for more details

