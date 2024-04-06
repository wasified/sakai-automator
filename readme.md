# Sakai Automator

Sakai Automator uses Playwright Python to automate Sakai - for testing or other purposes. It is very bare-bones right now, but in the longer-term each folder will contain automated versions of test scripts written by Andrea and the test team. In the ultra-longer term (lol) it would be cool if an NLP layer can be added - and a .txt document can be passed in and the Automator can run a 'tree' of interactions with the interface in various interactions and stuff.

Anyway, currently, you can use test_setup.py to quickly setup users and a site based on a CSV - which saves A LOT of time and makes you more productive as a QA person or a dev. It takes 30 seconds (might be faster if you run headless) to setup an instructor account, and a course site with all tools enabled and 23 users added - which I think is pretty cool. 

### Automatically creating accounts and a course site with test_setup.py 
Pip install playwright python, clone this repo, and just run 'pytest test_setup.py'. The script will do the following:

- Read a CSV - will treat the first user in the CSV as the instructor and the rest as students. 
- Login as admin, upload the CSV, and create the users in your CSV then log out
- Login then as the instructor, create a course site (name specificed in COURSE_NAME under test_setup)
- After creating the course site, it will add all of the students as users. 
- Will then log out. 



### Assignments folder

This is a work in progress which converts one of Andrea's test scripts into.py file that automates what a manual QA Tester would do. From the root folder you can run assignments/basic_post.py and the script will do the following:

- Signs as instructor (hence you need to run test_setup.py before you run this)
- Creates an assignment via an empty form, asserts if correct error message was displayed
- After asserting correct error message was displayed, adds in a proper title and description
- Adds an alpha character in Max Points, tries to post then asserts if correct error message was displayed
- Adds a number in Max Points, posts assignments
- Goes back to assignments page, and verifies that the assignment was published. 
- Logs out. 


### Users.csv

A users.csv is included, but you can switch to any valid CSV that you already use with Sakai. Currently, no error handling to ensure patten of reading the CSV - will add that later. 