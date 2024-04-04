from playwright.sync_api import Playwright, sync_playwright, expect
import os
import json
import csv

def get_user_list():
    file = open("users.csv")

    csvreader = csv.reader(file)

    header = []
    headr = next(csvreader)

    rows = []

    for row in csvreader:
        rows.append(row)

    instructor = row[0][0]

    students = []

    for col in range(1, len(rows)):
        user = rows[col][0]
        students.append(user)

    final_string = "\\n".join(students)
    return final_string

##def test_login_admin(playwright: Playwright) -> None:
##    global page, context, browser
##    browser = playwright.chromium.launch(headless=False, slow_mo = 50)
##    #context = browser.new_context()
##    # Create a new context with the saved storage state.
##    context = browser.new_context(storage_state="state-admin.json")
##
##    page = context.new_page()
##
##    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
##    page.get_by_placeholder("Username").click()
##    page.get_by_placeholder("Username").fill("admin")
##    page.get_by_placeholder("Username").press("Tab")
##    page.get_by_placeholder("Password").fill("admin")
##    page.get_by_placeholder("Password").press("Enter")
##
##    # Save storage state into the file.
##    #storage = context.storage_state(path="state-admin.json")
##
##
##
##def test_logout(playwright: Playwright) -> None:
##    #global page
##    page.get_by_role("button", name="Profile image").click()
##    page.get_by_role("link", name=" Log Out").click()
##    #context = browser.new_context(storage_state="state-admin.json")
##    #page = context.new_page()
##    #page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
##
##    # ---------------------
##    context.close()
##    browser.close()
