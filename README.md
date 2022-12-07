# Pet Groomer Central

> Python, HTML, Flask, SQLite, Bootstrap, Jinja.

## Project Overview
A dynamic Flask web application using Python3 and HTML that that handles user authentication (login, logout, registration) and allows pet groomers to create, modify, search, and delete appointments with made with clients.

Find the video demo here: https://youtu.be/TQ-hZR23kTc

Find the public GitHub repository here: https://github.com/jyliu11/Pet-Groomer-Central.git

### Features
* Web pages rendered with Jinja templating and styled with Bootstrap elements.
* Client information and appointment details stored into a relational SQLite database.
* Database records managed using SQLAlchemy and HTTP requests.


### How to Run the App
To run this application, first download this repository and open it in GitHub/VS Code.

(Assuming in Terminal) First, go into the folder:
```bash
cd [folderNameHere]
```

Next, install the necessary packages:
```bash
pip3 install -r requirements.txt
```

Then, enter:
```bash
export FLASK_APP=main.py
```

Finally, enter:
```bash
flask run
```

> Above command will create and activate the Flask web app

At start up, users may toggle the nagivation bar to switch between the Account Login and Registration Pages. Signed in/newly registered users will be greeted with their personal Home Page.