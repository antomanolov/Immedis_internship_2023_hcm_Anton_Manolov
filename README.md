
# Human Capital Management App Project by Anton Manolov

## The project is 2 major projects with 3 aps (1 frontend project with BFF API) and 1 backend API. The idea of the project was to have 2 UIs. One that is accessible for the HR(admin) and one that is made for the Employee. 

## What is done in the project:
### General login/logout system that is shared for the HRs and Employees

## HR side UI functionality with the backend:
### 1 HR can create/delete and modify users.
### 2 It can also assign tasks and reviews to any user.
### 3 HR can pay salaries. At first it was intended to be automatic, but in this prototype it will not happen. Manual entry of paycheck is still possible.
### 4 HR has the ability to see all their reviews.
### 5 Also they can see up to 10 users from each department, and search their details if necessary.
### 6 Currently, no one except HR can log into the site becouse of the is_hr atribute in the model.

## The employee for that moment doen't have functional UI, it is only static, but model wise everything is ready to be connected through the APIs.

## Things that I am proud of that I've neved done before:

### 1 Made the APIs, I've never done anything even close to this, and there are my pride and glory.
### 2 When an employee is created, a table for his leave days is also created by signal.
### 3 Login system from scratch, everything is custom made, even the Admin panel to Django.
### 4 Even after the massive change that I made to the architecture of the project I've managed to make the things work

## Things that will be made in future:
### 1 Completely different UI for employees (which is ready but not functional)
### 2 Every worker will be able to check in/check out.
### 3 Any worker will be able to post requests.
### 4 Each employee will be able to see all reviews written about it, as well as all paycheks, tasks and everything related to it by pk.
### 5 Automate the paycheck system
### 6 Make separate DBs for all data that will acumulate for the years to come.
### 7 Update the UI and put much more JS modals and validations.


