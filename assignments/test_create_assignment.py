#-------------------------------------------------------------------------------
# Name:        test_basic_post
# Purpose:
#
# Author:      lifel
#
# Created:     05/04/2024
# Copyright:   (c) lifel 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# This script translates the following test script:
#https://docs.google.com/spreadsheets/d/1D4ClvBNbPE7A5JIQyeB1_PbVT7UuxxnrVFWUlNwB0yc/edit?gid=2076185087#gid=2076185087
# comments have been added

from playwright.sync_api import Playwright, sync_playwright, expect
from utils import read_csv
import time

# docx report stuff
import io
from docx import Document
from docx.shared import Inches

report_docx = Document()
#report_docx.add_heading("Test Report", 0)
#report_docx.add_heading('Test run on: ', 3)

ASSIGNMENT_NAME = "Assignment D23"
COURSE_NAME = "VJ101"
URL = "https://trunk-mysql8.nightly.sakaiproject.org/"
instructor_id, instructor_pass = read_csv.get_instructor_credentials()

def test_create_assignment(playwright: Playwright) -> None:
    """
    This function goes from steps 1.01 to 1.08 in the
    basic_functionality_testing script.

    """
    global browser, context, page
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    screenshot_bytes = page.screenshot(type='png')
    #img = base64.b64encode(screenshot_bytes).decode()
    screenshot_file = io.BytesIO(screenshot_bytes)
    screenshot_file.seek(0)
    report_docx.add_picture(img, width=Inches(6))
    report_docx.save('test1.docx')
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(instructor_id)
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill(instructor_pass)
    page.get_by_placeholder("Password").press("Enter")
    #page.get_by_role("button", name="Expand tool list").click()
    #page.get_by_role("link", name="Assignments").click()
    #page.get_by_role("button", name="").click()
    #page.get_by_role("link", name="Okay, got it!").click()
    page.get_by_role("link", name="%s 1 1 Spring"%COURSE_NAME).click()
    page.get_by_role("link", name="Assignments").click()
    page.get_by_role("link", name="Add").click()
    page.get_by_role("button", name="Post").click()
    # assert empty form isn't published: 1.02 in the script
    expect(page.get_by_text("Alert: Please specify the assignment title")).to_be_visible()
    # take a screenshot
    page.get_by_placeholder("Title").click()
    page.get_by_placeholder("Title").fill(ASSIGNMENT_NAME)
    page.frame_locator("iframe[title=\"Editor\\, new_assignment_instructions\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Editor\\, new_assignment_instructions\"]").get_by_label("Editor,").fill("Sample description. ")
    page.get_by_placeholder("Title").press("Tab")
    page.get_by_label("Max Points").click()
    page.get_by_label("Max Points").fill("a")
    page.get_by_role("button", name="Post").click()

    # asserts error message: 1.06 in the script
    expect(page.get_by_text("Alert: Please use a number")).to_be_visible()
    page.get_by_label("Hide due date from students").check()
    page.get_by_label("Add an announcement about the").check()
    page.get_by_label("Max Points").click()
    page.get_by_label("Max Points").click(click_count=3)
    page.get_by_label("Max Points").fill("10")
    #page.locator("#assignmentGradingGradebookOptionsPanel div").click()
    page.get_by_role("button", name="Post").click()
    # asserts that assignement was created
    expect(page.get_by_role("cell", name="%s Edit Assignment"%ASSIGNMENT_NAME)).to_be_visible()
    page.get_by_role("button", name="Profile image").click()
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    #context.close()
    #browser.close()




##def test_view_assignment_as_student(playwright: Playwright) -> None:
##    #browser = playwright.chromium.launch(headless=False)
##    #context = browser.new_context()
##    #page = context.new_page()
##    page.goto(URL)
##    page.get_by_placeholder("Username").click()
##    page.get_by_placeholder("Username").fill("student1")
##    page.get_by_placeholder("Username").press("Tab")
##    page.get_by_placeholder("Password").fill("sakai")
##    page.get_by_placeholder("Password").press("Enter")
##    #page.get_by_role("button", name=" Click to dismiss").click()
##    #page.get_by_role("link", name="Okay, got it!").click()
##    page.get_by_role("button", name="Expand tool list").click()
##    page.locator("#pinned-site-list").get_by_role("link", name="Announcements").click()
##    #page.get_by_role("link", name="Assignment: Open Date for '%s'"%ASSIGNMENT_NAME).click()
##    page.get_by_role("link", name="Assignment: Open Date for ''%s'' Assignment: Open Date for ''"%ASSIGNMENT_NAME).click()
##    #1..09: Verify you see the announcement
##    expect(page.locator("#content div").filter(has_text="Open date for assignment ''").nth(3)).to_be_visible()
##    #navigate to assignments tool
##    page.get_by_role("link", name="Assignments").click()
##    # 1.10: assert date field is empty:
##    expect(page.get_by_role("rowgroup")).to_contain_text("")
##    # assert assignment name matches
##    #1.12: Verfiy the name of the assignment
##    expect(page.get_by_role("rowgroup")).to_contain_text(ASSIGNMENT_NAME)
##    # click on assignment submission page
##    page.get_by_role("link", name=ASSIGNMENT_NAME).click()
##    # 1.12: verify that due date is empty
##    expect(page.locator("#StudentAssignmentCurrent")).to_contain_text("")
##
##    # log out as student
##    page.get_by_role("button", name="Profile image").click()
##    page.get_by_role("link", name=" Log Out").click()
##
##    # ---------------------
##    #context.close()
##    #browser.close()
##
##def test_instructor_edits_assignment(playwright: Playwright):
##    browser = playwright.chromium.launch(headless=False)
##    context = browser.new_context()
##    page = context.new_page()
##    page.goto(URL)
##    page.get_by_placeholder("Username").click()
##    page.get_by_placeholder("Username").fill("qateacher")
##    page.get_by_placeholder("Username").press("Tab")
##    page.get_by_placeholder("Password").fill("sakai")
##    page.get_by_placeholder("Password").press("Enter")
##    page.get_by_role("button", name="Expand tool list").click()
##    page.get_by_role("link", name="Assignments").click()
##    page.get_by_role("link", name="Edit Assignment D11").click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Accept Until", exact=True).click()
##    page.get_by_label("Accept Until", exact=True).click()
##    page.get_by_label("Accept Until", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).press("ArrowRight")
##    page.get_by_label("Due Date", exact=True).fill("")
##    page.get_by_label("Due Date", exact=True).press("Control+z")
##    page.get_by_label("Due Date", exact=True).press("Control+z")
##    page.get_by_label("Due Date", exact=True).press("Control+z")
##    page.get_by_label("Due Date", exact=True).click()
##    page.get_by_label("Due Date", exact=True).press("ArrowLeft")
##    page.get_by_label("Due Date", exact=True).fill("2024-09-10T20:20")
##    page.get_by_label("Accept Until", exact=True).click()
##    page.get_by_label("Accept Until", exact=True).press("ArrowRight")
##    page.get_by_label("Accept Until", exact=True).fill("2024-09-11T20:20")
##    page.get_by_label("Hide due date from students").uncheck()
##    page.get_by_role("button", name="Post").click()
##    #2.02: Verify the date updated
##    expect(page.get_by_text("Sep 10, 2024, 8:20 PM")).to_be_visible()
##
##    # ---------------------

#with sync_playwright() as playwright:
#    run(playwright)
