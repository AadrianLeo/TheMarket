# TheMarket

## Introduction
TheMarket is an marketing website where you can buy sell any product with any category. Users can have conversation regaring the product from the owner directly through the website in the prodect section. A seller an uplaod the products details and edit anytime he wants. Every user has a secure login password to identify as a erticuler user. This website is Build using Django python.

#
## Documentation for access in you local servre and developement and changes 

#### Python 3.8 is recomended.

#### The website is user developement you can run the website in local server 

#### For running the website in local server :
Go to the path in themarket > themarket > settings.py

and comment the below code :

#### `ALLOWED_HOSTS = ['.vercel.app', '.now.sh']`

and uncomment the below code for getting the website on local server :

#### `ALLOWED_HOSTS = ['127.0.0.1']`

and comment the below code in the same file :

 #### `DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'HOST': "db.hxrfbdsvqkgsuatvdczi.supabase.co",
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "**********",
        'PORT': "5432",
    }
}`

and uncomment the below code for changing the database to db.sqlite3 :

#### `DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}`

before running the Below Commands activate the virtual envirenment to access python:
#### `# env\Scripts\activate`

and then run the below command in the terminal :
#### `# python manage.py makemigrations`

and then this command :
#### `# python manage.py migrate`

and run the website with the following command :
#### `# python manage.py runserver`

#

Thw website is not totaly ready for production working on some databse issue for image to upload.
If any issue comes up for the above documentaion try contacting me.
Fave Fun 😁 




