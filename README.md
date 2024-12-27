# 

## Import the sql file to Mysql

    1. Open folders

        db -> new db -> law.sql

    2. Import it to your Mysql to work

#
##  First  time only [1-5]

#### 1. Create Virtual Env 
      py -m venv myenv
      myenv\Scripts\activate

#### 2. Install Packages 
    
    pip install django
    pip install mysqlclient

#### 3. Migrate 
    py manage.py migrate

#### 4. Run Server
    py manage.py runserver

#### To Deactivate Virtual Env 
    deactivate


#
## To Run [1-2]

#### 1. Activate myenv
    myenv\Scripts\activate
#### 2. Run Server
    py manage.py runserver

#
## Admin Login 

    username: admin
    password: 123

