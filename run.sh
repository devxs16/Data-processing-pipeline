#!/bin/bash

source venv/bin/activate

pip install -r requirements.txt

cd assignment_site

python manage.py migrate

python manage.py runserver &
cd ..

python app/listener.py