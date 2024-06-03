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

ASSIGNMENT_NAME = "Assignment C"
COURSE_NAME = "VJ101"
instructor_id, instructor_pass = read_csv.get_instructor_credentials()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo= 100)
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
    # asset empty form isn't published
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
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
