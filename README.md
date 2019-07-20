# edu-platform
Cloud-based School Management Platform based on  Django and Angular

## Set up

Open the terminal (linux)

create and open a new folder

Clone the repo

```
git clone https://github.com/thiernomoudou/school-api.git

```

create a vitualenvironment

```
virtualenv yourVirtualenvName
```

```
source yourVirtualenvName/bin/activate
```

Enter the edu-platform folder

```
cd school-api
```

Install dependencies and setup data

```
pip install -r requirements.txt
```

we use python-decouple for environment variables
create a .env file in the root of the directory

```
touch .env
```


open the .env file and then set the secretkey  
for example type this command or set a new secretkey

```
SECRET_KEY=y83-5a2$3c)!88cieuwuwywopppp-382872
```

migrate all thes changes to the sqlite3 database
```
python manage.py migrate
```

create superuser account 

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

NB: if you don't have pip and virtualenv installed, 
    install them before typing these commands.


