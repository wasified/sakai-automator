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

from playwright.sync_api import Playwright, sync_playwright, expect
from utils import read_csv

ASSIGNMENT_NAME = "Assignment D7"
COURSE_NAME = "VJ101"
instructor_id, instructor_pass = read_csv.get_instructor_credentials()

def test_create_assignment(playwright: Playwright) -> None:
    global browser, context, page
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/")
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
    # assert empty form isn't published
    expect(page.get_by_text("Alert: Please specify the assignment title")).to_be_visible()
    page.get_by_placeholder("Title").click()
    page.get_by_placeholder("Title").fill(ASSIGNMENT_NAME)
    page.frame_locator("iframe[title=\"Editor\\, new_assignment_instructions\"]").locator("html").click()
    page.frame_locator("iframe[title=\"Editor\\, new_assignment_instructions\"]").get_by_label("Editor,").fill("Sample description. ")
    page.get_by_placeholder("Title").press("Tab")
    page.get_by_label("Max Points").click()
    page.get_by_label("Max Points").fill("a")
    page.get_by_role("button", name="Post").click()

    # asserts error message
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


def test_view_assignment_as_student(playwright: Playwright) -> None:
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context()
    #page = context.new_page()
    page.goto("https://trunk-mysql8.nightly.sakaiproject.org/portal")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("student1")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("sakai")
    page.get_by_placeholder("Password").press("Enter")
    #page.get_by_role("button", name=" Click to dismiss").click()
    #page.get_by_role("link", name="Okay, got it!").click()
    page.get_by_role("button", name="Expand tool list").click()
    page.locator("#pinned-site-list").get_by_role("link", name="Announcements").click()
    #page.get_by_role("link", name="Assignment: Open Date for '%s'"%ASSIGNMENT_NAME).click()
    page.get_by_role("link", name="Assignment: Open Date for ''%s'' Assignment: Open Date for ''"%ASSIGNMENT_NAME).click()
    expect(page.locator("#content div").filter(has_text="Open date for assignment ''").nth(3)).to_be_visible()
    #navigate to assignments tool
    page.get_by_role("link", name="Assignments").click()
    # assert date field is empty
    expect(page.get_by_role("rowgroup")).to_contain_text("")
    # assert assignment name matches
    #expect(page.get_by_role("strong")).to_contain_text(ASSIGNMENT_NAME)
    expect(page.get_by_role("rowgroup")).to_contain_text(ASSIGNMENT_NAME)
    # click on assignment submission page
    page.get_by_role("link", name=ASSIGNMENT_NAME).click()
    # assert that due date is empty
    expect(page.locator("#StudentAssignmentCurrent")).to_contain_text("")

    # log out as student
    page.get_by_role("button", name="Profile image").click()
    page.get_by_role("link", name=" Log Out").click()

    # ---------------------
    context.close()
    browser.close()



#with sync_playwright() as playwright:
#    run(playwright)
