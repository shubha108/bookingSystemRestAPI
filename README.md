<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h1 align="center">Booking System RestAPI</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/shubha108/bookingSystemRestAPI)](https://github.com/shubha108/bookingSystemRestAPI)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---
                       
<p align="center"> Few lines to describing my project.
    <br> 
</p>
                                     
## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Postman tests ](#postman)
- [Project Structure](#structure)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

In this project, I have created a booking system RestAPI that allows users to sign up, log in, and book a advisors with booking time and date and admin can add advisors. It also allows users to view their bookings. the system is built using Python, Django, MongoDB, and JWT authentication work properly and securely and to make it easy to use for the users and admins to use the system.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](https://www.geeksforgeeks.org/how-to-deploy-django-project-on-pythonanywhere/) for notes on how to deploy the project on a live system.
## 📦 Installation <a name = "installation"></a>


1.First you need to create a virtual environment
```
py -3 -m venv venv
```
```
cd venv pip install -r requirements.txt (The requirements for this project will be installed)
```

2.Project Setup

```
cd booking_system python manage.py migrate (this will migrate everythings)
```
 Now create superuser 
 ```
 python manage.py createsuperuser.
 ```

### Prerequisites <a name = "prerequisites"></a>

What things you need to install the software and how to install them.

```
pip install django, 
pip install djangorestframework, 
pip install djongo ,
pip install dnspython,
pip install django-cors-headers

```

## 🎈 Project Structure <a name="structure"></a>

* [Booking_system](booking_system/booking_system) Booking_System is the main project folder.
* [setting.py](booking_system/booking_system/settings.py) is the settings file for the project.
* [urls.py](booking_system/booking_system/urls.py) contains the url patterns for the bookedcalls app.
* [BookedCalls](booking_system/bookedcalls) Booked calls is the app.
* [urls.py](booking_system/bookedcalls/urls.py) is the url file that contains the urls for the api.
* [Views.py](booking_system/bookedcalls/views.py) is the views file that contains the views for the api.
* [Models.py](booking_system/bookedcalls/models.py) is the models file that contains the models for the api including the User ,Advisor as well as bookedCalls models.
* [Serializers.py](booking_system/bookedcalls/serializers.py) is the serializers file that contains the serializers for the api.

## 🔧 Postman API Tests <a name = "postman"></a>

### [Postman collections](./postmen_tests/bookingSystemAPI.postman_collection.json)


## Adding a new Advisor using POST /api/admin/advisor API.
 
 <img   alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/add_advisor.gif" />


## User can register using POST /api/user/register API.
 
 <img  alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/user_register.gif" />
 

## User login  using POST /api/user/login API.
  
  <img   alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/user_login.gif" />



## List of advisors by user_id using GET /api/user/user_id/advisors API.
  
   <img    alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/advisor_list.gif" />



## Book a call by user_id and advisor_id using POST user/userid/advisor/advisorid/book API.
 
   <img  alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/advisor_booking.gif" />



## Get all the booking of a user by user_id using GET user/userid/advisor/booking API.
 
   <img   alt="" src="https://raw.githubusercontent.com/shubha108/bookingSystemRestAPI /master/postmen_tests/img/user_bookings.gif" />
   
## ⛏️ Built Using <a name = "built_using"></a>

- [python](https://www.python.org/) - the programming language
- [Django](https://www.djangoproject.com/)  - the web framework
- [Django REST Framework](https://www.django-rest-framework.org/) - the framework for the API
- [Django Simple Auth](https://django-simple-auth.readthedocs.io/) - JWT Authentication.
- [MongoDB](https://www.mongodb.com/) - the database

## ✍️ Authors <a name = "authors"></a>

- [@Shubham Sharma](https://github.com/shubha108) - the author and maintainer of the project.


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

## References

- [Python Docs](https://Pythondocs.com/), 
- [Django Docs](https://www.djangoproject.com/), 
- [Django REST Framework ](https://www.django-rest-framework.org/),
- [Django Simple Auth docs](https://django-simple-auth.readthedocs.io/),
- [MongoDB Docs](https://www.mongodb.com/)
