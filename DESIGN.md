# Pet Groomer Central Design

## Rationale

I started exchanging letters with a penpal at the start of the pandemic. They live in Indonesia and their family runs a pet grooming business. I learned that they use paper for everything, recording clients, keeping track of appointments, organizing calendars, and so on, so I thought I'd use this opportunity to create something that could potentially assist them and their business, even in the smallest of ways. Thus, I came up with the idea of creating a simple and user-friendly website that could allow them to organize their information in a place where it wouldn't easily be lost.

## Back-End

### SQL and Javascript

I began with implementing an effective database system consisting of two tables:
- task: the unique id of the client (id), the client's name (username), appointment date (appt_date), the integer version of the appointment date (appt_date_int), the time for which the appointment is set (time), the unique id number of the pet groomer (user_id), and the status of the appointment (status)
- user: the unique id number of the user/pet groomer (id), usernames (username), password hashes (password), and first name (first_name)

The "user" table allows the web app to create and delete users, while the "task" table allows the web app the create, delete, and manage the clients and their appointments. Both were implemented fairly easily
with simple Python and Flask elements.

#### Application Requirements
The packages and libraries needed to run this web app are listed in the ```requirements.txt``` file.

### Python and Flask

In the "auth.py" file, the app routes implemented are detailed as follows:
- /login: quits current user's session, allows new user to log in; receives account information and checks with the "users" table to see if the user should be let into the rest of the web application.
- /logout: quits current user's session and returns the user to the login page.
- /register: allows new user to make an account; checks if inputted information is new to the "users" table and inserts into it.

In the "views.py" file, the app routes implemented are detailed as follows:
- /home: lands the user one the home page, where all of the client and appointment information can be found.
- /create: allows users to add new client and appointment information.
- /delete: allows users to delete existing clients/appointments.
- /update: allows users to update information and statuses of appointments.

The other ".py" files, including "__init__.py", "helpers.py", "models.py", and "main.py" all assist with other details, including creating and registering the blueprints, setting up the calendar and datetime features, arranging spects of the table, and creating the actual website.

## Front-End

### HTML

- "base.html" incorporates all of the boostrap elements used in the website, and sets up the basic tabs and alerts used throughout the website.
- "create.html" designs the elements that appear once a user wants to add a new client/appointment to the table, including the text boxes and confirmation/re-routing buttons.
- "home.html" handles everything on the main page once the user logs in, including the search bar, multiple alerts for restricted actions, the actual table where the appointments appear, the buttons at the bottom of the page, and more.
- "login.html" curates the login page, including the username and password boxes.
- "register.html" manages all of the features on the register page, including the boxes where the user enters their information, the directory text, as well as the rerouting link at the bottom if one already has an account.
- "update.html" handles everything on the page that appears once a user wishes to change an element of an existing appointment or client, including many of the same elements outlined in the "create.html" page.