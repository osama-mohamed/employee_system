# [Employee System](https://employee-osama-mohamed-django.herokuapp.com) By Django

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="Employee System" >](https://employee-osama-mohamed-django.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="Employee System" >](https://employee-osama-mohamed-django.herokuapp.com)



## For live preview :
> [Employee System Cards Layout](https://employee-osama-mohamed-django.herokuapp.com)


> [Employee System Table Layout](https://employee2-osama-mohamed-django.herokuapp.com)


## Employee System website contains:
### 1 App :
    1. Employees
    

* Add employee
* Edit employee
* Delete employee
* Add relation
* Edit relation
* Delete relation
* Show all relations for a married employee


## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. python manage.py migrate

2. python manage.py runserver

# if you want to manage to project just create super user account by :

3. python manage.py createsuperuser

```

That's it.

## Done :

Now the project is running at `http://localhost:8000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	   | Home page                                      |
| {host}/admin/  	                                           | GET      	   | Admin control panel                     	      |
| {host}/employees/                                          | GET      	   | Show all employees                         	  |
| {host}/employees/add/                                      | POST      	   | Add new employee                           	  |
| {host}/employees/{id}/                                     | GET      	   | Show employee detail                        	  |
| {host}/employees/{id}/update/                              | POST      	   | Update employee data                        	  |
| {host}/employees/{id}/update_salary/                       | POST      	   | Update employee salary                      	  |
| {host}/employees/{id}/delete/                              | POST      	   | Delete employee                            	  |
| {host}/employees/{id}/relations/                           | GET      	   | Show employee relations                     	  |
| {host}/employees/{id}/add_relation/                        | POST      	   | Add relation to employee                    	  |
| {host}/employees/{id}/update_relation/                     | POST      	   | Edit employee relation                      	  |
| {host}/employees/{id}/delete_relation/                     | POST      	   | Delete relation                            	  |


For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/1.11/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
