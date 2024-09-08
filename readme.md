# Sakai Automator

Sakai Automator uses Playwright Python to automate Sakai - for testing or other purposes. The project has two folder 'twothree' (for 23 related stuff) and 'twofour' (covers 24/25 (the most recent trunks)). 

### Running test
Install pre-reqs from requirements.txt, then run the following from the root:

- "pytest twofour/test_setup.py" - this will create user accounts. This will do the following:

    - Read a CSV - will treat the first user in the CSV as the instructor and the rest as students.
    - Login as admin, upload the CSV, and create the users in your CSV then log out
    - Login then as the instructor, create a course site (name specificed in COURSE_NAME under test_setup)
    - After creating the course site, it will add all of the students as users.
    - Log out.

    
- "pytest twofour/assignments/basic_functional_testing.py" - this will run the interactions as outlined in the  "basic functional tests"  sheet for the assignment tool as outlined in this test script: https://docs.google.com/spreadsheets/d/1D4ClvBNbPE7A5JIQyeB1_PbVT7UuxxnrVFWUlNwB0yc/edit?gid=2076185087#gid=2076185087 


### Extra Files

A users.csv is included, also a docx file to handle file uploading related scenarios. 
