# QuantEdge
A production-style Django platform for portfolio analytics, stock research, watchlists, alerts, and quantitative investment insights. Built while mastering Django engineering concepts from fundamentals to advanced backend architecture.

# Commands

python -m venv venv

pip install django

django-admin startproject quantedge .

python manage.py startapp common

get-ChildItem common

New-Item common/utils.py -ItemType File

git add .

git commit -m "message"

git push origin branch_name

git checkout -b branch_name

git diff branch1 branch2 --stat

git ls-tree --name-only -r branch_name

psql --version

pip install psycopg[binary]

pip install python-dotenv

pip freeze > requirements.txt

python manage.py check

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
